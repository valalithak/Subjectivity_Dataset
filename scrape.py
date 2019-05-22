from bs4 import BeautifulSoup
import requests
import datetime
from time import sleep
import os
# f = open('deepika_ranveer_ht.txt', 'w')
url = 'https://www.indiatoday.in/deepika-ranveer-wedding?page=2'
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "lxml")

b = soup.findAll('h2')
for link in b:
    c = link.find('a').get('href')
    print("https://www.indiatoday.in" + str(c))
