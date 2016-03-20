import urllib.request
from bs4 import BeautifulSoup
import re


def fetchUrl():
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel  Mac OS X 10_10_5) AppleWebKit/601.4.4 (KHTML, like Gecko)   Version/9.0.3 Safari/601.4.4')]
    site = opener.open(html)
    global bsObj
    bsObj = BeautifulSoup(site, "html.parser")
    return bsObj

def vgchartz():
    global html
    html = 'http://www.vgchartz.com/gamedb/?results=100'
    fetchUrl()
    t = open("vgchartz.txt", 'w')

    for game in bsObj.find('table', {'class':'chart'}).findAll('tr'):
        t.write(str(game.get_text()) + "\n")

    t.close()

def metacritic():
    global html
    html = 'http://www.metacritic.com/browse/games/score/metascore/all/all'
    fetchUrl()
    t = open("metacritic.txt", 'w')

    for game in bsObj.find('div', {'class':'product_rows'}).findAll('div', {'class':'product_title'}):
        t.write(game.get_text())

    t.close()

def howlong():
    global html
    html = 'http://howlongtobeat.com/stats_more.php?s=Most_Submissions'
    fetchUrl()
    t = open("howlongtobeat.txt", 'w')

    for game in bsObj.table.tbody.findAll('td', {'class':'left'}):
        t.write(str(game.get_text()))

    t.close()



vgchartz()
metacritic()
howlong()
