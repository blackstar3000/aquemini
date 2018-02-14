import requests
from bs4 import BeautifulSoup

url = "https://www.shesfreaky.com/"
r = requests.get(url)

soup = BeautifulSoup(r.content, "lxml")

links = soup.find_all("img")


# print(soup.prettify())"<a href='%s'>%s</a>" %(link.get("href"), link.text)link.get("href")img class="lazy" src="
for link in links:
    print "<a href='%s'>%s</a>" %(link.get("src"), link.text)
