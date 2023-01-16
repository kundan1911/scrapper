import os
import django

# os.environ.setdefault('DJANGO_SETTINGS_MODULE','scrapper_site.settings')
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

url ="https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&page=1&cityName=Mumbai&language=en"
response = requests.get(url)
response = response.content
soup = bs(response, 'html.parser')
cards = soup.find_all('div', class_='mb-srp__card')

i=0
locality = "None"
furnishing = "None"
carpet_area = "None"
facing = "None"
floor = "None"
tenant = "None"
bathrooms = "None"
status = "None"
transaction = "None"
society = "None"
desc = "None"
date_posted = "None"


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
        print(date_posted)
    except:
        posted_date = "None"
    try: 
        link = card.find('a', class_='mb-srp__card__society--name')['href']
    except:
        link = "None"
    try: 
        owner = card.find('div', class_='mb-srp__card__ads--name').text
    except:
        owner = "None"
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
        desc = "None"
    price = card.find('div', class_='mb-srp__card__price--amount').text.replace('₹', '')
    try: 
        per_sqft = card.find('div', class_='mb-srp__card__price--size').text.replace('₹', '')
    except:
        per_sqft = "None"
    for elem in childs.contents:
        try:
            if elem.get('data-summary') == 'facing':
                facing = elem.text.replace('facing', '')
        except:
            facing= "None"
        try:
            if elem.get('data-summary') == 'tenent-preffered':
                tenant = elem.text.replace('Tenant Preferred', '')
        except:
            tenant= "None"
        try:
            if elem.get('data-summary') == 'floor':
                floor = elem.text.replace('Floor', '')
        except:
            floor= "None"
        try:
            if elem.get('data-summary') == 'carpet-area':
                carpet_area = elem.text.replace('Carpet Area', '')
        except:
            carpet_area= "None"
        try:
            if elem.get('data-summary') == 'society':
                society = elem.text.replace('Society', '')
        except:
            society= "None"
        try:    
            if elem.get('data-summary') == 'furnishing':
                furnishing = elem.text.replace('Furnishing', '')  
        except:
            furnishing = "None"
        try: 
            if elem.get('data-summary') == 'bathroom':
                bathrooms = elem.text.replace('Bathroom', '')
        except:
            bathrooms = "None"
        try:
            if elem.get('data-summary') == 'status':
                status = elem.text.replace('Status', '')
        except:
            status = "None"
        try:
            if elem.get('data-summary') == 'transaction':
                transaction = elem.text.replace('Transaction', '')
        except:
            transaction = "None"
    entry=Entries(id=i,Date_Posted=date_posted, Link=link, Owner=owner,bHK=bhk,Locality=locality,city='Mumbai',Price=price,Carpet_Area=carpet_area,Furnishing=furnishing,Bathrooms=bathrooms,Facing=facing,Status=status,Transaction=transaction,Price_Sqft=per_sqft,Floor=floor,Description=desc)
    entry.save()
###
    #  print(e)
    i=i+1;

        # except:
        #     print("except")
    # bhks = card.find('h2', class_='mb-srp__card--title').text
    
   