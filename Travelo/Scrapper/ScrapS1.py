from ast import keyword
from asyncio.windows_events import NULL
import difflib
from random import randint
from bs4 import BeautifulSoup as bs
import pandas as pd
import urllib.request
from datetime import date, datetime

# def locater(l) :
#     loc = ['Afghanistan','Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Democratic People's Republic of", 'Korea, Republic of', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe']
#     Loca = difflib.get_close_matches(l, loc)
#     Location = Loca[0]
#     return Location

# def dateFct(d) :
#     string = d
#     format_ddmmyyyy = "%d/%m/%Y"
#     dater = datetime.strptime(string, format_ddmmyyyy)
#     if dater :
#         return dater 
#     else :  
#         return 'NULL'

# #holiday
# def ScrapSite4(url):
#     headers = {'User-Agent ' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/E7FBAF'}
#     TripList = []
#     r=urllib.request.urlopen(url,timeout=50)
#     soup = bs(r,'lxml')

#     voyages = soup.find_all('div', {'class': 'row products'})
#     voyagesLinks = [] 
#     for v in voyages :
#         for link in v.find_all('a',href = True) :
#             voyagesLinks.append(link['href'])
#     voyagesLinks = ["https://www.holidaypure.com"+s for s in voyagesLinks]
               
    
#     for link in voyagesLinks:
#         r=urllib.request.urlopen(link,timeout=50)
#         soup = bs(r,'lxml')
#         try :
#          Name = soup.find('h1' , {'class' : 'font-20 font-weight-bold mb-2 align-self-center'}).text.strip()
#         except :
#          Name = 'NaN'
#         try :
#          tag = soup.find('span' , {'class' : 'price font-20'}).text.strip()
#          tag = tag.replace('\n' , '')
#          tag = [int(s) for s in tag.split() if s.isdigit()]
#          price = tag[0]

#         except :
#          price = 0

#         Date_dep = 'NULL'
#         t = Name.split()[:1]
#         Locat = t[0]
#         if Locat == 'Istanbul' :
#             Location = 'Turkey'
#         elif Locat == 'Antalya' :
#             Location = 'Turkey'
#         elif Locat == 'Sharm' :
#             Location == 'Egypt'
#         elif Locat == 'Malte' :
#             Location = 'Malta'
#         else :
#             Location = 'Autre'
        
#         LocationS = t[0]
       
#         try :
#           Offer = soup.find('div',{'class' : 'services'}).text.strip()   
#         except :
#           Offer = Name
#         try : 
#           tage = soup.find('div',{'class' : 'col-md-9 align-items-center'}).text.strip()  
#           tage = [int(s) for s in tage.split() if s.isdigit()] 
#           if tage[0] < 10 :
#            duration = tage[0]
#           else :
#             duration = tage[1]
#         except :
#            duration = 'NaN'
     
#         logo = 'https://yt3.ggpht.com/ytc/AKedOLQZJTLMRBGKGy2ZqkSpLwejm86FYz0YQIP5x99Tqw=s900-c-k-c0x00ffffff-no-rj'
#         site = 'holidaypure.com'
        
      
#         a={'Name' : Name ,'Type' : 'Voyage' ,'Location' : Location ,'price' : price,'LocationS' : LocationS ,'Offer':Offer ,'Date_dep' : Date_dep ,'Duration' : duration ,'Url' : link ,'img' : logo,'Site' : site}  
#         TripList.append(a)


   
#     df = pd.DataFrame.from_dict(TripList)
 
#     return df

    

# ###liberta
# def ScrapSite3(url):
#     headers = {'User-Agent ' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/E7FBAF'}
#     ### Accesing Source
#     r=urllib.request.urlopen(url,timeout=50)
#     soup = bs(r,'lxml')
#     keywords = ['Antalya' , 'Bursa' , 'Istanbul' , 'Marakech' , 'Fethiye' , 'Maroc' , 'Madrid' , 'Brésil' , 'Zanzibar' , 'Morocco']
#     Location = []
#     ### Accessing Links
#     voyages = soup.find_all('div', {'class': 'img_container'})
#     voyagesLinks = [] 
#     for v in voyages :
#         for link in v.find_all('a',href = True) :
#             voyagesLinks.append(link['href'])
            
#     voyagesLinks = ["https://www.libertavoyages.com"+s for s in voyagesLinks]        
    
#     Prices = []
#     price = soup.find_all('div' , {'class' : 'price_grid'})
#     for r in price :
#      r = r.text
#      r = r.replace('\n','')
#      r = r.replace(' ','')
#      r =  r.translate({ord(i): None for i in 'abcdefghijklmnopqrstuvwxyzàSA/TND'})
#      if r == 'nan' :
#         r == 1000
#         Prices.append(r)
#      else :
#       Prices.append(r)

#     duration = []
#     Sites = []
#     imgs = []
#     Type = []
#     Names = []
#     Name = soup.find_all('h4', {'style' : 'margin-bottom: 0px;display: inline;'})
#     for n in Name :
#         n = n.text 
#         n = n.replace('\n','')
#         n = n.strip()
#         Names.append(n)
#         Type.append('Voyages')
#         imgs.append('https://www.libertavoyages.com/file_manager/source/front/logo_header.png')
#         Sites.append('libertavoyages.com')
#         duration.append(randint(6,9))
        
  
   
#     LocationS = []
#     loc = soup.find_all('div' , {'class' : 'short_info'})
#     for t in loc :
#       t = t.find('em')
#       try :
#         t = t.text
#         t = t.strip()
#         t = t.replace("\n",'')
#         t = t.replace('Turquie','Turkey')
#         Location.append(t)
#       except :
#         Location.append("Autre")
#         LocationS.append("Autre")
      
      
    
#     date_dep = []
#     off = soup.find_all('div' , {'class' : 'desc'})
#     for l in off :
#      try :
#         l = soup.find('em')
#         l = l.text
#         l = l.replace('\n','')
#         l = l.split(' ')
#         l = l[-1]
#         #[print(x) for x in keywords if x in l]
#         date_dep.append(l)
#      except :
#         date_dep.append('NULL')   

#     a={'Name' : Names ,'Type' : Type ,'Location' : Location ,'LocationS' : Location ,'price' : Prices,'Offer':Names ,'Date_dep' : date_dep ,'Duration' : duration ,'Url' : voyagesLinks ,'img' : imgs,'Site' : Sites}        
    
#     df = pd.DataFrame.from_dict(a, orient='index')
#     df = df.transpose()
#     return df
#     # ### Merging then saving 
#     # merged = df.join(df1)
#     # merged.to_csv("3s.csv", index=False, encoding='utf-8')
#     # return merged

# # #SAFARIVoyage
# def ScrapSite2(Url):

#     TripList = []
#     headers = {'User-Agent ' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/E7FBAF'}
#     ### Accesing Source
#     url = Url
#     re=urllib.request.urlopen(url,timeout=50)
#     soup = bs(re,'lxml')
    
#     ### Accessing Links
#     voyages = soup.find_all('div', {'class': 'card result_item animation'}) 
#     voyagesLinks = [] 
#     for v in voyages :
#         for link in v.find_all('a',href = True) :
#             voyagesLinks.append(link['href'])

#         voyagesLinks = [e.replace(' ','%20') for e in voyagesLinks]
#         voyagesLinks = [e.replace('é','e') for e in voyagesLinks]
#         voyagesLinks = list(dict.fromkeys(voyagesLinks))
#     ### Accessing Data
#     for link in voyagesLinks:
        
#         r=urllib.request.urlopen(link,timeout=50)
#         soup = bs(r,'lxml')
     
#         try :
#          Name = soup.find('h1' , {'class' : 'product_name'}).text.strip()
#         except :
#          Name = 'NaN'
#         try : 
#          price = soup.find('div', {'class' : 'price'}).text.strip().replace('DT','') 
#         except : 
#          price = 1000
#         try :
#          Location = soup.find('span',{'class' : 'destination'}).text.strip().replace('Tunisie','').lstrip(',')
#          if Location == 'Turquie' :
#             Location = 'Turkey'
#          elif Location == 'Egypte,' or 'Egypt' :
#             Location = 'Egypt'
#          elif Location =='Tanzanie, République-unie De,' :
#             Location = 'Tanzania' 
#          elif Location =='Morocco,' :
#             Location = 'Morroco'  
#          else :  
#              pass
#         except :
#          Location = 'NaN'
#         try :
#          tag = soup.find('div',{'class' : 'content_box'})
#          tag = tag.li.text.replace('\n','').replace('                                               ',' ').lstrip('Du')
#          tag = tag.strip()[:2]
#          tag = str(tag)+'/08/2022'
#          Date_dep = dateFct(tag)
#          Date_dep = str(Date_dep).strip()[:10]
        
#         except :
#          Date_dep = 'NULL'
#         try :
#          LocationS = Location
#         except :
#          LocationS = Location
#         try :
#           Offer = soup.find('div',{'class' : 'typevoyage'}).text.strip()   
#         except :
#           Offer = 'NaN'
#         try : 
#            duration = randint(6,9)                                             
#         except :
#            duration = 'NaN'
      
#         logo = 'https://prod.bravebooking.net/clients/SV76920/media/photos/website/logo_1_safarivoyages.svg'
#         a={'Name' : Name ,'Type' : 'Voyage' ,'Location' : Location ,'LocationS' : LocationS ,'Offer':Offer ,'Date_dep' : Date_dep ,'price' : price ,'Duration' : duration ,'Url' : link ,'img' : logo,'Site' : 'SafariVoyage.com'}
#         TripList.append(a)
  
#     df = pd.DataFrame.from_dict(TripList)
#     return df

# #TRAVELToDO
# def ScrapSite1(Url):

#     TripList = []
#     header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/E7FBAF'}
#     ### Accesing Source
#     url = Url
#     r=urllib.request.urlopen(url,timeout=50)
#     soup = bs(r,'lxml')
#     import requests
#      ### Accessing prices 
#     ps = []
#     price = soup.find_all('span' , {'class' : 'fs-4 font-weight-600'})
#     for e in price :
#         e=e.text
#         e=e.replace('\n','')
#         e=e.strip("TND")
#         ps.append(e)

#     b = {'price' : ps }
#     df1 = pd.DataFrame.from_dict(b, orient='index')
#     df1 = df1.transpose()
#     ##df1.to_csv('prices.csv', index=False, encoding='utf-8')  
 
#     ### Accessing Links
#     voyages = soup.find_all('div', {'class': 'col-md-6'}) 
#     voyagesLinks = [] 
#     for v in voyages :
#         for link in v.find_all('a',href = True) :
#             voyagesLinks.append(link['href'])
#     ### Accessing Data
#     for link in voyagesLinks:
#         r=urllib.request.urlopen(link,timeout=500)
#         soup = bs(r,'lxml')
#         try :
#          Name = soup.find('h1' , {'class' : 'cr_title4'}).text.strip()
#         except :
#          Name = 'NaN'
#         try : 
#          r = soup.find('span', {'class' : 'cr_title1'}).text.strip() 
#          Date_dep = dateFct(r)
#          Date_dep = str(Date_dep).strip()[:10]
#          if Date_dep == '':
#             Date_dep = ('')
#         except : 
#          Date_dep ='NULL'
#         try :
#          Location = soup.find('a',{'id' : 'ProductSummary1_HyperLink_Destination'}).text.strip() 
#         except :
#          Location = 'NaN'
#         try :
#          LocationS = soup.find('a',{'id' : 'ProductSummary1_HyperLink_CityArrival'}).text.strip() 
#         except :
#          LocationS = Location
#         try :
#           Offer = soup.find('td',{'style' : 'cursor:pointer;border-right: #828282 1px solid;'}).text.strip()   
#         except :
#           Offer = 'NaN'
#         try : 
#           tage = soup.find('span',{'id' : 'ProductSummary1_Label_Duration_Display'}).text.strip()  
#           tage = [int(s) for s in tage.split() if s.isdigit()] 
#           duration = tage[0]
#         except :
#            duration = 'NaN'
     
#         logo = 'https://www.traveltodo.com/dist/img/logo.png'
       
#         a={'Name' : Name ,'Type' : 'Voyage' ,'Location' : Location ,'LocationS' : LocationS ,'Offer':Offer ,'Date_dep' : Date_dep ,'Duration' : duration ,'Url' : link ,'img' : logo,'Site' : 'Traveltodo.com'}  
#         TripList.append(a)
  
#     df = pd.DataFrame.from_dict(TripList)
#     ##df.to_csv('', index=False, encoding='utf-8')
#     ### Merging then saving 
#     merged = df.join(df1)
#     # merged.to_csv(fileName, index=False, encoding='utf-8')
#     return merged


# def merger () :
   
#     cs = "date_on/scrapped_in_"+str(date.today())+".csv"

#     m1 = ScrapSite1('https://www.traveltodo.com/sejours-etrangers/packages/')
#     m2 = ScrapSite1('https://www.traveltodo.com/sejours-etrangers/sejours-a-petit-prix/')
#     m3 = ScrapSite1('https://www.traveltodo.com/sejours-etrangers/packages-de-luxe/')
#     m4 = ScrapSite2('https://www.safarivoyages.tn/index.php?cmd=sejour&action=list&type=4') 
#     m5 = ScrapSite3('https://www.libertavoyages.com/VoyageOrganise/liste')
#     m6 = ScrapSite3('https://www.libertavoyages.com/VoyageOrganise/liste/1/2')
#     m7 = ScrapSite4('https://www.holidaypure.com/voyages-organises/')

#     merged = pd.concat([m1,m2,m3,m4,m5,m6,m7]) 
#     merged.to_csv(cs, index=False, encoding='utf-8')
#     merged.to_csv('TTD.csv', index=False, encoding='utf-8')
#     return merged

# merger()   
 

# def tester():
#     url = 'https://www.traveltodo.com/'
#     r=urllib.request.urlopen(url,timeout=50)
#     soup = bs(r,'lxml')
#     logo = soup.find('a' ,{'class' : 'navbar-brand'})
#     for l in logo.find('img' , src = True) :
#      print(l)
# tester()

  
def readercsv ():
    
    data = pd.read_csv (r'C:\Users\WIKI\projets\TestingApplication\TTD.csv')   
    df = pd.DataFrame(data)
    print(df)
    return df

