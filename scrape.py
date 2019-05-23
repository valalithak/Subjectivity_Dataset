from bs4 import BeautifulSoup
import requests
import datetime
from time import sleep
import os
# f = open('deepika_ranveer_ht.txt', 'w')
url = 'https://timesofindia.indiatimes.com/topic/Priyanka-Nick-Wedding/news/3'
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "lxml")

b = soup.findAll('div', attrs = {'class':'content'})
for link in b:
    c = link.find('a').get('href')
    print("https://timesofindia.indiatimes.com" + str(c))
