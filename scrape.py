from bs4 import BeautifulSoup
import requests
import datetime
from time import sleep
import os
# f = open('deepika_ranveer_ht.txt', 'w')
url = 'https://www.hindustantimes.com/topic/maharashtra-plastic-ban'
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "lxml")

b = soup.findAll('div', attrs = {'class':'authorListing'})
for link in b:
    c = link.find('a').get('href')
    print(c)
