# -*- coding: utf-8 -*-
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
                try:
                    article = soup.findAll('div', attrs = {'class':' '})
                    paras = article[3].findAll('div')[0].text
                    
                    new_path = ('/').join(path.split('/')[:-1]) + '/hindu_article_' + str(idx + 1) + '.txt'
                    f = open(new_path, 'w')
                    f.write(paras.encode('utf-8'))
                    f.close()
                except:
                    pass
                sleep(2)
        
def indianexpress():
    nyt_paths = commands.getoutput("find -name *indianexpress.txt").split('\n')
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
                headline = soup.findAll('h1')[0].text
                print headline
                content = " "
                b = soup.findAll('div', attrs = {'itemprop': 'articleBody'})
                for text in b:
                    c = text.findAll('p')
                    content += str(c)
                
               
                clean = re.compile('<.*?>')
                content = re.sub(clean, '', content)
                clean = re.compile('</p>')
                content = re.sub(clean, '', content)
                
        
                article = content.text
                new_path = ('/').join(path.split('/')[:-1]) + '/indianexpress_article_' + str(idx + 1) + '.txt'
                f = open(new_path, 'w')
                f.write(headline.encode('utf-8') + '\n')
                f.write(article.encode('utf-8'))
                f.close()
                sleep(2)
                
                   
def ht():
    nyt_paths = commands.getoutput("find -name *ht.txt").split('\n')
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
                headline = soup.findAll('h1')[0].text
                print headline
                paras = soup.findAll('p')
                
                content = " "
                for i in range(0, len(paras)-1):
                    article = paras[i].text
                    content += article + "\n"

                article = content
                new_path = ('/').join(path.split('/')[:-1]) + '/ht_article_' + str(idx + 1) + '.txt'
                f = open(new_path, 'w')
                f.write(headline.encode('utf-8') + '\n')
                f.write(article.encode('utf-8'))
                f.close()
                sleep(2)
              

def bbc():
    nyt_paths = commands.getoutput("find -name *bbc.txt").split('\n')
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
                headline = soup.findAll('h1')[0].text
                print headline
                paras = soup.findAll('p')
                
                content = " "
                for i in range(11, len(paras)-3):
                    article = paras[i].text
                    content += article + "\n"
                
                # print content
                article = content
                new_path = ('/').join(path.split('/')[:-1]) + '/bbc_article_' + str(idx + 1) + '.txt'
                f = open(new_path, 'w')
                f.write(headline.encode('utf-8') + '\n')
                f.write(article.encode('utf-8'))
                f.close()
                sleep(2)            
                
def toi():
    nyt_paths = commands.getoutput("find -name *toi.txt").split('\n')
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
                headline = soup.findAll('h1')[0].text
                print headline
                paras = soup.findAll('div', attrs = {'class': '_3WlLe clearfix '})
                
                try:
                    article = paras[0].text
                    #print article
                    new_path = ('/').join(path.split('/')[:-1]) + '/toi_article_' + str(idx + 1) + '.txt'
                    f = open(new_path, 'w')
                    f.write(headline.encode('utf-8') + '\n')
                    f.write(article.encode('utf-8'))
                    f.close()
                except:
                    pass
                sleep(2)

def mathrubhumi():
    nyt_paths = commands.getoutput("find -name *mathrubhumi.txt").split('\n')
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
                headline = soup.findAll('h1')[0].text
                print headline
                paras = soup.findAll('div', attrs = {'class': 'col-md-12 col-sm-12 col-xs-12'})
                # print paras

                content = " "
                for i in range(0, len(paras)):
                    article = paras[i].find('p').text
                    print article 
                for i in paras:
                    article = i.find('p').text
                    print "article is :"
                    print article
                    print article
                    content += article + "\n"
                
                print content
                # article = paras[0].text
                # print article
                # new_path = ('/').join(path.split('/')[:-1]) + '/mathrubhumi_article_' + str(idx + 1) + '.txt'
                # f = open(new_path, 'w')
                # f.write(headline.encode('utf-8') + '\n')
                # f.write(article.encode('utf-8'))
                # f.close()
                sleep(2)               

def mylaporetimes():
    nyt_paths = commands.getoutput("find -name *mylaporetimes.txt").split('\n')
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
                headline = soup.findAll('h2')[0].text
                print headline
                content = " "
                paras = soup.findAll('div', attrs = {'class': 'recent post'})
                for i in range(0, len(paras)):
                    article = paras[i].findAll('p')
                for i in article:
                    content += i.text + "\n"

                article = content   
                new_path = ('/').join(path.split('/')[:-1]) + '/mylaporetimes_article_' + str(idx + 1) + '.txt'
                f = open(new_path, 'w')
                f.write(headline.encode('utf-8') + '\n')
                f.write(article.encode('utf-8'))
                f.close()
                sleep(2)

def dc():
    nyt_paths = commands.getoutput("find -name *Deccanchronicle.txt").split('\n')
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
                headline = soup.findAll('h1')[0].text
                print headline
                paras = soup.findAll('p')
                
                content = " "
                for i in range(0, len(paras)-1):
                    article = paras[i].text
                    content += article + "\n"
                
                # print content
                article = content
                new_path = ('/').join(path.split('/')[:-1]) + '/DC_article_' + str(idx + 1) + '.txt'
                f = open(new_path, 'w')
                f.write(headline.encode('utf-8') + '\n')
                f.write(article.encode('utf-8'))
                f.close()
                sleep(2) 
def jakarta():
    nyt_paths = commands.getoutput("find -name *jakarta*").split('\n')
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
                headline = soup.find('h1', attrs = {'class': 'title-large'}).text
                print headline
                paras = soup.findAll('p')
                
                content = " "
                for i in range(5, len(paras)-1):
                    article = paras[i].text
                    content += article + "\n"
                
                # print content
                article = content
                new_path = ('/').join(path.split('/')[:-1]) + '/jakartapost_article_' + str(idx + 1) + '.txt'
                f = open(new_path, 'w')
                f.write(headline.encode('utf-8') + '\n')
                f.write(article.encode('utf-8'))
                f.close()
                sleep(2) 

def ani():
    nyt_paths = commands.getoutput("find -name *ani*").split('\n')
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
                headline = soup.find('h1').text
                print headline
                paras = soup.findAll('p')[1].text
                print paras
                # content = " "
                # for i in range(0, len(paras)):
                #     article = paras[i].text
                #     content += article + "\n"
                
                # print content
                article = paras
                new_path = ('/').join(path.split('/')[:-1]) + '/ani_article_' + str(idx + 1) + '.txt'
                f = open(new_path, 'w')
                f.write(headline.encode('utf-8') + '\n')
                f.write(article.encode('utf-8'))
                f.close()
                sleep(2) 

def guardian():
    nyt_paths = commands.getoutput("find -name *guardian*").split('\n')
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
                headline = soup.find('h1').text
                print headline
                paras = soup.findAll('p')
                
                content = " "
                for i in range(5, len(paras)-1):
                    article = paras[i].text
                    content += article + "\n"
                
                # print content
                article = content
                new_path = ('/').join(path.split('/')[:-1]) + '/guardian_article_' + str(idx + 1) + '.txt'
                f = open(new_path, 'w')
                f.write(headline.encode('utf-8') + '\n')
                f.write(article.encode('utf-8'))
                f.close()
                sleep(2) 

def telegraphindia():
    nyt_paths = commands.getoutput("find -name *telegraphindia.txt").split('\n')
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
                headline = soup.find('h1').text
                print headline
                paras = soup.findAll('p')
                
                content = " "
                for i in range(0, len(paras)-7):
                    article = paras[i].text
                    content += article + "\n"
                
                # print content
                article = content
                new_path = ('/').join(path.split('/')[:-1]) + '/local_article_' + str(idx + 1) + '.txt'
                f = open(new_path, 'w')
                f.write(headline.encode('utf-8') + '\n')
                f.write(article.encode('utf-8'))
                f.close()
                sleep(2) 

def mysore():
    nyt_paths = commands.getoutput("find -name *mysore.txt").split('\n')
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
                headline = soup.find('h1').text
                print headline
                paras = soup.findAll('span')
                
                content = " "
                for i in range(0, len(paras)-7):
                    article = paras[i].text
                    content += article + "\n"
                
                print content
                # article = content
                # new_path = ('/').join(path.split('/')[:-1]) + '/local_article_' + str(idx + 1) + '.txt'
                # f = open(new_path, 'w')
                # f.write(headline.encode('utf-8') + '\n')
                # f.write(article.encode('utf-8'))
                # f.close()
                sleep(2) 

def independent():
    nyt_paths = commands.getoutput("find -name independent.txt").split('\n')
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
                headline = soup.find('h1')
                print headline
                paras = soup.findAll('p')
                
                content = " "
                for i in range(0, len(paras)):
                    article = paras[i].text
                    content += article + "\n"
                
                print content
                # article = content
                # new_path = ('/').join(path.split('/')[:-1]) + '/independent_article_' + str(idx + 1) + '.txt'
                # f = open(new_path, 'w')
                # f.write(headline.encode('utf-8') + '\n')
                # f.write(article.encode('utf-8'))
                # f.close()
                sleep(2) 

def france24():
    nyt_paths = commands.getoutput("find -name france24.txt").split('\n')
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
                headline = soup.find('h1').text
                print headline
                paras = soup.findAll('span')
                
                content = " "
                for i in range(0, len(paras)-7):
                    article = paras[i].text
                    content += article + "\n"
                
                print content
                # article = content
                # new_path = ('/').join(path.split('/')[:-1]) + '/local_article_' + str(idx + 1) + '.txt'
                # f = open(new_path, 'w')
                # f.write(headline.encode('utf-8') + '\n')
                # f.write(article.encode('utf-8'))
                # f.close()
                sleep(2) 
               
# indiat()
#nyt()
# et()
#hindu()
#indianexpress()
# ht()
# bbc()
toi()
# mathrubhumi()
# mylaporetimes()
# dc()
# jakarta()
# ani()
# guardian()
# telegraphindia()
# mysore()
# independent()
#france24()
