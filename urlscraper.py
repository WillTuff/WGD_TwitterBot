import urllib2
import csv
import os
from bs4 import BeautifulSoup

os.chdir("/Users/willtuff/Python/Twitter Bots/Test1 (MinganiTwitBots)")

csv_file = open('list.csv', 'wr')
writer = csv.writer(csv_file)

url='https://www.youtube.com/playlist?list=PLYai4fwN_q5Z739RBuo5f6_X3cPJ4jETF'
html=urllib2.urlopen(url)
response=html.read()
soup=BeautifulSoup(response, "lxml")

links = soup.find_all('a', attrs={'class':'pl-video-title-link'})

for link in links:
    urlEntry = []
    vidStr = link.get('href')
    urlEntry.append((vidStr))
    writer.writerow(urlEntry)

for a in urlEntry:
    print str(urlEntry)

csv_file.close()
