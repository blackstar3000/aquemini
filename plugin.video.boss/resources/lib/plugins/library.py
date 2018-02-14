import xbmc
import xbmcaddon
import xbmcgui
import xbmcvfs
from koding import route
from resources.lib.util.url import get_addon_url
from resources.lib.util.xml import JenItem
from ..plugin import Plugin

addon_fanart = xbmcaddon.Addon().getAddonInfo('fanart')
addon_icon = xbmcaddon.Addon().getAddonInfo('icon')
addon_name = xbmcaddon.Addon().getAddonInfo('name')
addon_id = xbmcaddon.Addon().getAddonInfo('id')


class Library(Plugin):
    name = "Add To Library"

    def get_context_items(self, item, context):
        if not xbmc.getCondVisibility("system.hasaddon(plugin.video.metalliq)"):
            return
        jen_item = item
        identifier = None
        meta = jen_item.get("meta", None)
        if meta:
            meta = JenItem(meta)
            tvdb = meta.get("tvdb", None)
            if tvdb and tvdb != "0":
                identifier = tvdb
            else:
                imdb = meta.get("imdb", None)
                if imdb and imdb != "0":
                    identifier = imdb
                else:
                    tmdb = meta.get("tmdb", None)
                    if tmdb and tmdb != "0":
                        identifier = tmdb
        if not identifier:
            return

        content = jen_item["content"]

        if content == "movie":
            context.append(("Add To Library",
                           "RunPlugin({0})".format(
                               get_addon_url("add_to_library",
                                             {
                                                 "media_type": "movies",
                                                 "identifier": identifier
                                             }))))
            return context
        elif content == "tvshow":
            context.append(("Add To Library",
                           "RunPlugin({0})".format(
                               get_addon_url("add_to_library",
                                             {
                                                 "media_type": "tvshow",
                                                 "identifier": identifier
                                             }))))
            return context


@route(mode="add_to_library", args=["media_type", "identifier"])
def add_to_library(media_type, identifier):
    player_id = addon_id.split(".")[-1]
    player = "direct.%s" % player_id
    if not install_player():
        return    
    if media_type == "movies":
        if identifier.startswith("tt"):
                src = "imdb"
        else:
            src = "tmdb"

        metalliq_path = "plugin://plugin.video.metalliq/movies/add_to_library_parsed/%s/%s/%s" % (src, identifier, player)
        xbmc.executebuiltin('RunPlugin(%s)' % (metalliq_path))
    elif media_type == "tvshow":
        metalliq_path = "plugin://plugin.video.metalliq/tv/add_to_library_parsed/%s/%s" % (identifier, player)
        xbmc.executebuiltin('RunPlugin(%s)' % (metalliq_path))

def install_player():
    player_id = addon_id.split(".")[-1]
    player = "direct.%s" % player_id
    metalliq_profile = xbmcaddon.Addon("plugin.video.metalliq").getAddonInfo('profile')
    metalliq_player_path = metalliq_profile + "players/%s.metalliq.json" % player
    addon_path = xbmcaddon.Addon().getAddonInfo('path')
    addon_player_path = addon_path + "/%s.metalliq.json" % player
    if not xbmcvfs.exists(addon_player_path):
            return False
        
    if not xbmcvfs.exists(metalliq_player_path):        
        if not xbmcgui.Dialog().yesno(addon_name, "Install metalliq player?"):
            return False
        xbmcvfs.copy(addon_player_path, metalliq_player_path)

    return True
        
