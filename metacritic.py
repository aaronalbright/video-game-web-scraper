import urllib.request
from bs4 import BeautifulSoup
import re

def page1():
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.4.4 (KHTML, like Gecko) Version/9.0.3 Safari/601.4.4')]
    html = opener.open('http://www.metacritic.com/browse/games/score/metascore/all/all')
    bsObj = BeautifulSoup(html, "html.parser")

    t1 = open("metacritic_page1.txt", 'w')

    for game in bsObj.find('div', {'class':'product_rows'}).findAll('div', {'class':'product_title'}):
        t1.write(game.get_text())

    t1.close()

def page2():
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    html = opener.open('http://www.metacritic.com/browse/games/score/metascore/all/all?page=1')
    bsObj = BeautifulSoup(html, "html.parser")
    t2 = open("metacritic_page2.txt", 'w')

    for game in bsObj.find('div', {'class':'product_rows'}).findAll('div', {'class':'product_title'}):
        t2.write(game.get_text())

    t2.close()

page1()
page2()
