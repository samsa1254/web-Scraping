from django.db import models
import time

class Travel(models.Model) :
    Name = models.CharField(max_length=150,blank=True, null=True)
    Type = models.CharField(max_length=100,blank=True, null=True)
    Location = models.CharField(max_length=100,blank=True, null=True)
    LocationS = models.CharField(max_length=100,blank=True, null=True)
    Prices = models.FloatField(blank=True, null=True)
    Offer = models.CharField(max_length=1500,blank=True, null=True)
    image = models.CharField(max_length=300,blank=True, null=True)
    url = models.CharField(max_length=300,blank=True, null=True)
    duration = models.CharField(max_length=20,blank=True, null=True)
    date_dep = models.CharField(max_length=20,blank=True, null=True)
    site = models.CharField(max_length=20,blank=True, null=True)
    
        
    class Meta:
        abstract = False

class historique(Travel) :
   
    dated_on = models.DateField(auto_now=False, auto_now_add=True, null=True)
    
class vol(models.Model) :
    aero = models.CharField(max_length=150,blank=True, null=True)
    heure_dep = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    heure_arr = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    diff = models.CharField(max_length=100,blank=True, null=True)
    prices = models.FloatField(blank=True, null=True)
    site = models.CharField(max_length=1500,blank=True, null=True)
    image = models.CharField(max_length=300,blank=True, null=True)
    url = models.CharField(max_length=300,blank=True, null=True)
    dep = models.CharField(max_length=150,blank=True, null=True)
    arr = models.CharField(max_length=150,blank=True, null=True)

class reco (models.Model) :
    ip = models.CharField(max_length=100,blank=True, null=True)
    location = models.CharField(max_length=100,blank=True, null=True)
    country = models.CharField(max_length=100,blank=True, null=True)
    counter = models.IntegerField(blank=True, null=True)
    nom  = models.CharField(max_length=100,blank=True, null=True)
    fm   = models.BooleanField(blank=True, null=True)

