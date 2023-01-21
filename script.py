import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scrapper_site.settings')
django.setup()

import requests
import datetime
import nums_from_string
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import requests
from myapi.models import Entries

today = datetime.datetime.today().strftime ('%Y-%m-%d')
def get_date_posted(ago_count):
  Previous_Date = datetime.datetime.today() - datetime.timedelta(days=ago_count)
  previous_d_for = Previous_Date.strftime ('%d/%m/%Y')
  return previous_d_for

data = []
cities=['Mumbai']
property_option=['sale','Rent']

i=0

for pro_opt in range(0,2):
    for city_opt in range(0,1):
        url ="https://www.magicbricks.com/property-for-"+property_option[pro_opt]+"/residential-real-estate?bedroom=2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName="+cities[city_opt]+"&language=en"
        for pgNo in range(0,11):
            url =url+"&page="+str(pgNo)
            response = requests.get(url)
            response = response.content
            soup = bs(response, 'html.parser')
            cards = soup.find_all('div', class_='mb-srp__card')

            locality = "Null"
            furnishing = "Null"
            carpet_area = "Null"
            facing = "Null"
            floor = "Null"
            tenant = "Null"
            bathrooms = "Null"
            status = "Null"
            transaction = "Null"
            society = "Null"
            desc = "Null"
            date_posted = "Null"

            for card in cards:
                try:
                    posted_date = card.find(class_="mb-srp__card__photo__fig--post").text
                    if 'today' in posted_date or 'Today' in posted_date:
                        date_posted = get_date_posted(0)
                    elif 'ago' in posted_date:
                        ago_date_count = int(nums_from_string.get_nums(posted_date)[0])
                        if 'days' in posted_date:
                            date_posted = get_date_posted(ago_date_count)
                        elif 'weeks' in posted_date:
                            date_posted = get_date_posted((ago_date_count*7))
                        else:
                            date_posted = get_date_posted((ago_date_count*30))
                    elif 'yesterday' in posted_date or 'Yesterday' in posted_date:
                        date_posted = get_date_posted(1)
                    else:
                        date_posted = posted_date.replace('Posted: ','')
                except:
                    posted_date = "Null"
                try: 
                    link = card.find('a', class_='mb-srp__card__society--name')['href']
                except:
                    link = "Null"
                try: 
                    owner = card.find('div', class_='mb-srp__card__ads--name').text
                except:
                    owner = "Null"
                bhks = card.find('h2', class_='mb-srp__card--title').text
                prop_locality = bhks.split(', ')
                bhk = prop_locality[0][0:5]
                del prop_locality[0]
                try:
                    locality = prop_locality[0]
                except:
                    locality = 'Mumbai'
                childs = card.find('div', class_='mb-srp__card__summary__list')
                description = card.find('div', class_='mb-srp__card--desc')
                try: 
                    desc = description.find('p').text.replace('"', '')
                except:
                    desc = "Null"
                price = card.find('div', class_='mb-srp__card__price--amount').text.replace('₹', '')
                try: 
                    per_sqft = card.find('div', class_='mb-srp__card__price--size').text.replace('₹', '')
                except:
                    per_sqft = "Null"
                for elem in childs.contents:
                    try:
                        if elem.get('data-summary') == 'facing':
                            facing = elem.text.replace('facing', '')
                    except:
                        facing= "Null"
                    try:
                        if elem.get('data-summary') == 'tenent-preffered':
                            tenant = elem.text.replace('Tenant Preferred', '')
                    except:
                        tenant= "Null"
                    try:
                        if elem.get('data-summary') == 'floor':
                            floor = elem.text.replace('Floor', '')
                    except:
                        floor= "Null"
                    try:
                        if elem.get('data-summary') == 'carpet-area':
                            carpet_area = elem.text.replace('Carpet Area', '')
                    except:
                        carpet_area= "Null"
                    try:
                        if elem.get('data-summary') == 'society':
                            society = elem.text.replace('Society', '')
                    except:
                        society= "Null"
                    try:    
                        if elem.get('data-summary') == 'furnishing':
                            furnishing = elem.text.replace('Furnishing', '')  
                    except:
                        furnishing = "Null"
                    try: 
                        if elem.get('data-summary') == 'bathroom':
                            bathrooms = elem.text.replace('Bathroom', '')
                    except:
                        bathrooms = "Null"
                    try:
                        if elem.get('data-summary') == 'status':
                            status = elem.text.replace('Status', '')
                    except:
                        status = "Null"
                    try:
                        if elem.get('data-summary') == 'transaction':
                            transaction = elem.text.replace('Transaction', '')
                    except:
                        transaction = "Null"
                entry=Entries(id=i,Date_Posted=date_posted,Proptype=property_option[pro_opt], Link=link, Owner=owner,bHK=bhk,Locality=locality,city=cities[city_opt],Price=price,Carpet_Area=carpet_area,Furnishing=furnishing,Bathrooms=bathrooms,Facing=facing,Status=status,Transaction=transaction,Price_Sqft=per_sqft,Floor=floor,Description=desc)
                entry.save()
                i=i+1;
    
   
   
