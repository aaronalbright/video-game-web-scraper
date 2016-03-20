import urllib.request
from bs4 import BeautifulSoup
import re

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.4.4 (KHTML, like Gecko) Version/9.0.3 Safari/601.4.4')]
html = opener.open('http://howlongtobeat.com/stats_more.php?s=Most_Submissions')
bsObj = BeautifulSoup(html, "html.parser")

t = open("howlongtobeat.txt", 'w')


for game in bsObj.table.tbody.findAll('td', {'class':'left'}):
    t.write(str(game.get_text()))


t.close()
