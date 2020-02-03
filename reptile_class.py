#!/usr/bin/env python
# coding=utf-8

from bs4 import BeautifulSoup
import urllib
url = ""
response = urllib.request.urlopen(url)
html = response.read()
bs = BeautifulSoup(html, "html.parser")
h1 = bs.find("span", class_="content-wrap")
print(h1.text)
next = bs.find("a", id = "j_chapterNext")
print(next.text)
print(next.['href'])

url1 = "https:" + next['href']  


