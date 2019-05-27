from bs4 import BeautifulSoup
import requests
import datetime
from time import sleep
import os
import commands
import re

def nyt():
    nyt_paths = commands.getoutput("find -name *nytimes*").split('\n')
    for path in nyt_paths:
        f = open(path, 'r')
        urls = f.readlines()
        f.close()
        for idx, url in enumerate(urls):
            if url != '\n':
                print url.strip()
                r = requests.get(url.strip())
                data = r.text
                soup = BeautifulSoup(data, "lxml")
                paras = soup.findAll('p', attrs = {'class': ['css-18icg9x', 'evys1bk0']})
                article = ''
                for para in paras:
                    article += para.text + ' '
                new_path = ('/').join(path.split('/')[:-1]) + '/nyt_article_' + str(idx + 1) + '.txt'
                f = open(new_path, 'w')
                f.write(article.encode('utf-8'))
                f.close()
                sleep(2)

def indiat():
    nyt_paths = commands.getoutput("find -name *indiatoday*").split('\n')
    for path in nyt_paths:
        f = open(path, 'r')
        urls = f.readlines()
        f.close()
        for idx, url in enumerate(urls):
            if url != '\n':
                print url.strip()
                r = requests.get(url.strip())
                data = r.text
                soup = BeautifulSoup(data, "lxml")
                headline = soup.findAll('h1', itemprop='headline')[0].text
                paras = soup.findAll('div', attrs = {'class': ['description']})
                article = paras[0].text
                new_path = ('/').join(path.split('/')[:-1]) + '/indiat_article_' + str(idx + 1) + '.txt'
                f = open(new_path, 'w')
                f.write(headline.encode('utf-8') + '\n')
                f.write(article.encode('utf-8'))
                f.close()
                sleep(2)

def hindu():
    nyt_paths = commands.getoutput("find -name *hindu.txt").split('\n')
    for path in nyt_paths:
        f = open(path, 'r')
        urls = f.readlines()
        f.close()
        for idx, url in enumerate(urls):
            if url != '\n':
                print url.strip()
                r = requests.get(url.strip(), allow_redirects = False)
                data = r.text
                soup = BeautifulSoup(data, "lxml")
                
                content = " "
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
                
                new_path = ('/').join(path.split('/')[:-1]) + '/hindu_article_' + str(idx + 1) + '.txt'
                f = open(new_path, 'w')
                f.write(content.encode('utf-8'))
                f.close()
                sleep(2)
        
                
#indiat()
#nyt()
hindu()
