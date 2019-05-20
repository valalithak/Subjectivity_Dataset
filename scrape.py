from bs4 import BeautifulSoup
import requests
import datetime
from time import sleep
import os

url = 'https://timesofindia.indiatimes.com/city/thiruvananthapuram/half-of-kerala-reels-under-floods-as-29-die-54000-are-homeless/articleshow/65362118.cms'
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "lxml")
headline = soup.find('div', attrs = {'class': '_38kVl'})
# print(headline)
date = headline.find('div', attrs = {'class': '_3Mkg- byline'})
for text in date:
    print(text)
headline2 = headline.find('h1')
for text in headline2:
    print(text)

a = soup.find('div', attrs = {'class':'_3WlLe clearfix '})

# print(a)
s = ""
for text in a:
    if str(text) == "<br/>":
        continue
    elif str(text).find("<") != -1:
        continue
    else:
      s += str(text)

print(s) 