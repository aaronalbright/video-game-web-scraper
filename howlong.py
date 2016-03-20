import urllib.request
from bs4 import BeautifulSoup
import re
import csv

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.4.4 (KHTML, like Gecko) Version/9.0.3 Safari/601.4.4')]
html = opener.open('http://howlongtobeat.com/stats_more.php?s=Most_Submissions')
bsObj = BeautifulSoup(html, "html.parser")

table = bsObj.find('table')
rows = table.findAll('tr')

csvFile = open("howlongtobeat.csv", 'wt')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll('td'):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()
