from django.urls import path

from Travelo.models import Travel
from . import views


urlpatterns = [
path('',views.fetchQuarries,name = 'home'),
path('contact/',views.CTC,name='ctc'),
path('price/',views.Prices,name='pr'),
path('dest/<str:loc>',views.getdest,name='dest'),
path('dest/',views.flambo,name='flam')
]
