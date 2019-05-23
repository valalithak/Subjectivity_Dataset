from bs4 import BeautifulSoup
import requests
import datetime
from time import sleep
import os
# f = open('deepika_ranveer_ht.txt', 'w')
url = 'https://www.thehindu.com/search/?q=section%20377%20verdict&order=DESC&sort=score&page=2'
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "lxml")

b = soup.findAll('a', attrs = {'class':'story-card75x1-text'})
for link in b:
    c = link.get('href')
    print(str(c))
