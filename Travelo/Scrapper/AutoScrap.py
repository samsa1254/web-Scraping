from bs4 import BeautifulSoup as bs
import pandas as pd
import urllib.request
import requests
import re

def Scrapip(ip):
   
    r=requests.get('https://db-ip.com/'+str(ip))
    soup = bs(r.content,'lxml')
    spl_word = 'Country'
    ip = soup.find('div', {'class': 'title head'}).text
    print(ip)
    s = ip.split()
    print(s)
    y = s[-1]
    if y == 'location':
     y = 'Tunisia'
    print(y)
    return(y)

   


