from bs4 import BeautifulSoup
import requests
import datetime
from time import sleep
import os
# f = open('deepika_ranveer_ht.txt', 'w')
url = 'https://www.thehindu.com/search/?q=karnataka%20elections%202018&order=DESC&sort=score&page=4'
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "lxml")

b = soup.findAll('div', attrs = {'class':'story-card story-card75x1-cont'})
for link in b:
    c = link.find('a').get('href')
    print(c)
