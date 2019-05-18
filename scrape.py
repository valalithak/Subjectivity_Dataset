from bs4 import BeautifulSoup
import requests
import datetime
from time import sleep
import os

#event_name= input()
#f = open('/home/lalitha/Desktop/events_dataset/' + str(event_name) + '_nytimes.txt', 'w')
#url = 'https://www.thehindu.com/search/?q=meghan markle wedding&order=DESC&sort=publishdate&page=1'
url = 'https://english.mathrubhumi.com/search?q=sabarimala'
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "lxml")
# for link in soup.find_all('a'):
#     if 'html' in link.get('href'):
#         f.write(link.get('href') + '\n')
# f.close()
a = soup.findAll('div', attrs={'class':'gsc-resultsRoot gsc-tabData gsc-tabdActive'})
print(a)

