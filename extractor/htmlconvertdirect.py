#!/usr/bin/env python

from urllib.request import urlopen
import html2text

from bs4 import BeautifulSoup

import requests
import urllib.request

link = "https://www.architecture.com/FindAnArchitect/FAAPractices.aspx?display=50"

html = requests.get(link).text

soup = BeautifulSoup(html, "lxml")

res = soup.findAll("article", {"class": "listingItem"})

for r in res:
    print(r.find_all("div", {'class': 'pageMeta-item'})[3].text)

