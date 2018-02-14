# -*- coding: utf-8 -*-

"""
    messages.py ---
    Copyright (C) 2017, Midraal

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import xbmcaddon
import random


def get_link_message():
    """
    helper function to get a random message when selecting links
    """
    import random
    messages = [
        {'HD': 'If Available',
         'SD': 'Most Likely Works'
         },
        {'HD': 'Boss\'s Ya Uncle',
         'SD': 'Boss\'s NOT Ya Cousin'
         },
        {'HD': 'Checking Top Sites',
         'SD': 'Sitting In Cinema Recording'
         },
        {'HD': 'This quality is being looked for by top men, who? Top....Men!',
         'SD': 'This quality is sold on the corner by a shady guy'
         },
        {'HD': 'Google Fiber',
         'SD': 'Waiting For Dialup Connection'
         },
        {'HD': 'Great! Worth the wait',
         'SD': 'Good Enough. I just want to watch'
         },
        {'HD': 'BluRay Quality',
         'SD': 'VHS Quality'
         },
        {'HD': 'I must see this film in the highest quality',
         'SD': 'Flick probably sucks so lets just get it over'
         },
        {'HD': 'Looks like a Maserati',
         'SD': ' Looks like a Ford Focus'
         },
        {'HD': 'Supermodel Quality',
         'SD': ' Looks like Grandma Thelma'
         },
        {'HD': 'Merc the pinnacle of brilliance',
         'SD': 'The john harrison of quality'
         },
    ]

    if xbmcaddon.Addon().getSetting('enable_offensive') == 'true':
        messages.extend([
            {'HD': 'Kicks Ass!!',
             'SD': 'Gets ass kicked repeatedly'
             },
            {'HD': 'Fucking Rocks!!',
             'SD': 'Fucking Sucks!!'
             },
            {'HD': 'Big Bodacious Breasts',
             'SD': 'Saggy Milk Teats',
             },
        ])

    if xbmcaddon.Addon().getSetting('disable_messages') == 'true':
        message = {
            'HD': 'If Available',
            'SD': ''
        }
    else:
        message = random.choice(messages)
    return message


def get_searching_message(preset):
    """
    helper function to select a message for video items
    Args:
        preset: search quality preset ("HD", "SD" or None)
    Returns:
        random message for video items
    """
    if xbmcaddon.Addon().getSetting('disable_messages') == "true":
        return ' '
    messages = [
        '',
        'Boss\'s just nipping to blockbusters won\'t be but a sec',
        'Boss fell asleep during this flick',
        'Boss\'s movie collection has no limits',
        'Searching the Internet for your selection',
        'Boss has seen your taste in movies and is very disappointed ',
        'Boss thinks he\'s got that DVD laying around here',
        'Boss says you\'re a movie geek just like him',
        'Boss says get off of twitter and enjoy his addon',
        'Boss is a wanted man in 125 countries',
        'Boss said your taste in films is top notch',
        'When Boss chooses a movie, servers shake in fear',
        'They fear Boss. Don\'t listen to haters',
        'Boss said he works so hard for YOU, the end user',
        'Boss does this cause he loves it, not for greed',
        'That\'s not Bosss butt crack, it\'s his remote holder',
        'Boss...I Am Your Father!!',
        'I\'m going to make Boss an offer he can\'t refuse.',
        'Here\'s looking at you, Boss',
        'Go ahead, make Boss\'s day.',
        'May the Boss be with you',
        'You talking to Boss??',
        'I love the smell of Boss in the morning',
        'Boss, phone home',
        'Made it Boss! Top of the World!',
        'Boss, James Boss',
        'There\'s no place like Boss',
        'You had me at "Boss"',
        "YOU CAN\'T HANDLE THE Boss",
        'Round up all the usual Bosss',
        'I\'ll have what Boss\'s having',
        'You\'re gonna need a bigger Boss',
        'Boss\'ll be back',
        'If you build it. Boss will come',
        'We\'ll always have Boss',
        'Boss, we have a problem',
        'Say "hello" to my little Boss',
        'Boss, you\'re trying to seduce me. Aren\'t you?',
        'Elementary, my dear Boss',
        'Get your stinking paws off me, you damned dirty Boss',
        'Here\'s Boss!',
        'Hasta la vista, Boss.',
        'Soylent Green is Boss!',
        'Open the pod bay doors, Boss.',
        'Yo, Boss!',
        'Oh, no, it wasn\'t the airplanes. It was Beauty killed the Boss.',
        'A Boss. Shaken, not stirred.',
        'Who\'s on Boss.',
        'I feel the need - the need for Boss!',
        'Nobody puts Boss in a corner.',
        'I\'ll get you, my pretty, and your little Boss, too!',
        'I\'m Boss of the world!',
        'Shan of Boss',
        'Bøb, Bøb, Bøb, Bøb, Bøb, Bøb, Bøb, Bøb, Bøb, Bøb, Bøb, Bøb',
        'We can rebuild Boss, we have the technology',
    ]

    if xbmcaddon.Addon().getSetting('enable_offensive') == "true":
        messages.extend([
            'Fuck Shit Wank -- Costa',
            'Frankly my dear, I don\'t give a Boss',
            'Beast Build Detected, Installing dangerous pyo file',
            'Costa wants to aduse Emma'
        ])

    if preset == "search":
        messages.extend([
            'Boss is popping in Blu Ray Disc'
        ])
    elif preset == "searchsd":
        messages.extend([
            'Boss rummaging through his vhs collection',
        ])

    return random.choice(messages)
