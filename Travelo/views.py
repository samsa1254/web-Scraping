
from asyncio.windows_events import NULL
from random import random
from typing import Counter
import pandas as pd
from django.shortcuts import render

from Travelo.Scrapper.AutoScrap import Scrapip
from .Scrapper.ScrapS1 import readercsv
from Travelo.models import Travel, reco
from .filters import OrderFilter
import socket
from django.db.models import F

def index(request):
    return render(request, 'index.html')

def dest(request):
    return render(request,'destination.html')

def Prices(request):
    return render(request,'pricing.html')

def CTC(request):
     return render(request,'contact.html')



def Localisation() :
    hostname=socket.gethostname()   
    IPAddr=socket.gethostbyname(hostname)
   
    return hostname,IPAddr


def truncate (clss):

 try  :
  clss.objects.all().delete()
  print('Reseting')
 except :
  print('erreur Truncate')

def addToDb(dff):
  truncate(Travel)
  for row in dff.itertuples():
    try :
        TravelObj = Travel.objects.create(Name = row.Name,Type = row.Type,Location = row.Location,
        LocationS = row.LocationS,Prices = row.price,
        Offer = row.Offer,url = row.Url,date_dep = row.Date_dep,duration = row.Duration,image = row.img,site = row.Site)
    except :
        pass
# addToDb(readercsv())

def fetchFromDb():
    Travels = []
    Travels = Travel.objects.all()
    return Travels


def fetchQuarries(request):
    f = Localisation()
    ip = f[1]
    host = f[0]
    fav = getmost(host)
    pric = Travel.objects.filter(Location = fav).order_by('Prices').first()

    travelDest = []
    travelDest = Travel.objects.values_list('Location', flat=True).distinct()
    context = {'T' : travelDest , 'ip' : ip , 'host' : host , 'fav' : fav , 'pric' : pric}
    return render(request,'index.html' , context)

def getdest (request , loc):
    host = request.GET['host']
    ip = request.GET['ip']
    print(ip)
    ctr = Scrapip(ip)
    print(ctr)
    ##getrecc()
    dima=Travel.objects.filter(Location = loc).order_by('Prices')
    check(loc , host , ip , ctr)
    context = {'T' : dima }
    return render(request,'destination.html' , context) 

def add(request):
   print('this is the request :',request)
   val1=request.GET['loc']
   dima=Travel.objects.filter(Location = val1)
   return render(request,'destination.html' , {'T' : dima})  


def getrecc(ctr) :
    a = reco.objects.filter(country = ctr).order_by('-counter').first()
    if a :
        return a.location
    else :
        pass
 

def flambo(request):

    flam = []
    flam = Travel.objects.all().order_by('Prices')[:5]
    return render(request,'destination.html' , {'T' : flam}) 

def check(loc , no , ip , ctr) :

    print(ctr)
    a = reco.objects.filter(nom = no, location = loc)
    if a :
       reco.objects.filter(nom = no , location = loc).update(counter = F('counter') + 1)
    else :
       reco.objects.create(nom = no , location = loc , counter = 1 , ip = ip , country = ctr)

def getmost(hosts) :
 a = reco.objects.filter(nom = hosts).order_by('-counter').first()
 if a :
    return a.location
 else : 
    pass 
 




