from bs4 import BeautifulSoup
import requests
import datetime
from time import sleep
import os
import re

# f = open('deepika_ranveer_ht.txt', 'w')
url = 'https://www.thehindu.com/business/Economy/at-stroke-of-midnight-india-gets-a-good-and-simple-tax/article19190299.ece'
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "lxml")
content = ""
b = soup.findAll('div', attrs = {'class':' '})
for text in b:
    c = text.findAll('p')
    content += str(c)

# print(content)
clean = re.compile('<.*?>')
content = re.sub(clean, '', content)
clean = re.compile('</p>')
content = re.sub(clean, '', content)

content = content.replace(".,", ".\n")
print(content)
