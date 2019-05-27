import re
import requests
import csv
from bs4 import BeautifulSoup
pages_url=['https://english.mathrubhumi.com/news/india/opening-of-dams-did-not-cause-floods-central-water-commission-1.3095222?fbclid=IwAR1RQ4SJ-ggVBQhdT25xQs0jKEjOStyu0LIN6nB5vaIySOhf01ONRBs5H9I']
NumComments = []
CommentText = []
rate = []
cost = []
numb  = []
href = []

for j in pages_url:
    #r = requests.get('https://www.amazon.in/gp/bestsellers/books/')
    r = requests.get(j)

    soup= BeautifulSoup(r.text, 'html.parser')
    # items = soup.findAll('li', {"class":"ThreadedConversation--loneTweet"})
    # k =  soup.findAll('div', {"class":"ThreadedConversation--loneTweet"})
    # l =  soup.findAll('li', {"class":"ThreadedConversation--loneTweet"})
    # m =  soup.findAll('div', {"class":"ThreadedConversation--loneTweet"})

  

    # dates = soup.findAll('div', {"class":"common_text_en date_outer"})
    # text = soup.findAll('div', {"class":"articleBody common_text"})
    body_ = soup.findAll('div', {"class":"articleBody common_text"})
    # title= soup.findAll('h1', {"class":"title"})
    
    # print title
    print "\n"
    print body_
    # print dates
    # print text