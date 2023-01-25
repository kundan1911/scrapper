from django.shortcuts import render
from rest_framework import viewsets
from myapinew.serializers import *
# from .models import *

# Create your views here.
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scrapper_site.settings')
django.setup()

import requests
import datetime
import nums_from_string
from bs4 import BeautifulSoup as bs
import requests
from .models import res_sale_model,res_pg_model,res_rent_model,comm_lease_model,comm_sale_model
# models for every type of sector(sale ,rent ,PG etc)

today = datetime.datetime.today().strftime ('%Y-%m-%d')
def get_date_posted(ago_count):
  Previous_Date = datetime.datetime.today() - datetime.timedelta(days=ago_count)
  previous_d_for = Previous_Date.strftime ('%d/%m/%Y')
  return previous_d_for


# the required cities data 
cities=['Mumbai', 'Gurgaon','Noida','Ghaziabad','Greater-Noida','Bangalore','Pune','Hyderabad','Kolkata','Chennai',
        'New-Delhi','Ahmedabad','Navi-Mumbai','Thane','Faridabad','Bhubaneswar','Bokaro-Steel-City','Vijayawada','Vrindavan', 'Bhopal',
        'Gorakhpur','Jamshedpur','Agra','Allahabad','Jodhpur''Aurangabad','Jaipur','Mangalore','Nagpur','Guntur','Navsari','Palghar','Salem','Haridwar','Durgapur',
        'Madurai','Manipal','Patna','Ranchi','Raipur','Sonipat','Kottayam','Kozhikode','Thrissur','Tirupati','Trivandrum','Trichy','Udaipur','Vapi','Varanasi',
        'Vadodara','Visakhapatnam','Surat','Kanpur','Kochi','Mysore','Goa','Bhiwadi','Lucknow','Nashik','Guwahati','Chandigarh','Indore','Coimbatore','Dehradun']
# cities=['Mumbai']

def str_sale_dt_db():
    i=0
    for city_opt in cities:
        URL ="https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName="+city_opt+"&language=en"
        for pgNo in range(0, 11):
            URL = URL+"&page="+str(pgNo)
            response = requests.get(URL)
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
                    locality = city_opt
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
                entry=res_sale_model(Id=i, Date_Posted=date_posted, Proptype='sale', Link=link, Owner=owner, BHK=bhk, Locality=locality, City=city_opt, Price=price, Carpet_Area=carpet_area, Furnishing=furnishing, Bathrooms=bathrooms, Facing=facing, Status=status, Transaction=transaction, Price_Sqft=per_sqft, Floor=floor, Description=desc)
                entry.save()
                i=i+1
        
def str_rent_dt_db():
    i=0
    for city_opt in cities:
        URL = "https://www.magicbricks.com/property-for-rent/residential-real-estate?bedroom=2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName="+city_opt+"&language=en"
        for pgNo in range(0, 11):

            URL = URL+"&page="+str(pgNo)
            response = requests.get(URL)
            response = response.content
            soup = bs(response, 'html.parser')
            cards = soup.find_all('div', class_='mb-srp__card')

            locality = 'Null'
            furnishing = 'Null'
            carpet_area = 'Null'
            facing = 'Null'
            floor = 'Null'
            tenant = 'Null'
            car_parking = 'Null'
            society = 'Null'
            desc = 'Null'
            date_posted = 'Null'

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
                    locality = city_opt
                childs = card.find('div', class_='mb-srp__card__summary__list')
                description = card.find('div', class_='mb-srp__card--desc')
                try: 
                    desc = description.find('p').text.replace('"', '')
                except:
                    desc = "Null"
                rent = card.find('div', class_='mb-srp__card__price--amount').text.replace('₹', '')
                for elem in childs.contents:
                    try:
                        if elem.get('data-summary') == 'facing':
                            facing = elem.text.replace('facing', '')
                    except:
                        facing= 'Null'
                    try:
                        if elem.get('data-summary') == 'tenent-preffered':
                            tenant = elem.text.replace('Tenant Preferred', '')
                    except:
                        tenant= 'Null'
                    try:
                        if elem.get('data-summary') == 'floor':
                            floor = elem.text.replace('Floor', '')
                    except:
                        floor= 'Null'
                    try:
                        if elem.get('data-summary') == 'society':
                            society = elem.text.replace('Society', '')
                    except:
                        society= 'Null'
                    try:    
                        if elem.get('data-summary') == 'furnishing':
                            furnishing = elem.text.replace('Furnishing', '')  
                    except:
                        furnishing = 'Null'
                    try: 
                        if elem.get('data-summary') == 'parking':
                            car_parking = elem.text.replace('Car Parking', '')
                    except:
                        car_parking = 'Null'
                    try:
                        if elem.get('data-summary') == 'carpet-area':
                            carpet_area = elem.text.replace('Carpet Area', '')
                    except:
                        carpet_area= 'Null'
                entry=res_rent_model(Id=i, Date_Posted=date_posted, Proptype='rent', Link=link, Owner=owner, BHK=bhk, Locality=locality, City=city_opt, Rent=rent, Carpet_Area=carpet_area, Furnishing=furnishing, Facing=facing, Tenant=tenant, Floor=floor, Description=desc)
                entry.save()
                i=i+1

def str_pg_dt_db():
    i=0

    for city_opt in cities:
        URL = "https://www.magicbricks.com/property-for-rent/residential-paying-guest?cityName=" + city_opt

        response = requests.get(URL)
        response = response.content
        soup = bs(response, 'html.parser')
        cards = soup.find_all('div', class_='m-srp-card')

        posted_by = 'Null'
        sharing_type = []
        pg_for = 'Null'
        charges = 'Null'
        pg_name = 'Null'
        link = 'Null'
        locality = 'Null'
        desc = 'Null'
        date_posted = 'Null'

        for card in cards:
            pg_for = card.find('span', class_='m-srp-card__info__gender').text

            try:
                link = card.find(attrs={'itemprop': 'url'})
                link = 'https://www.magicbricks.com/' + link.get('content')
            except:
                link = None

            res = requests.get(link)
            res = res.content
            res_soup = bs(res, 'html.parser')

            dep_amt = res_soup.find('div', class_='pg-prop-details__info__grid--value').text.replace('₹', '')

            try: 
                pg_name = card.find('meta', attrs={'itemprop': 'name'})
                pg_name = pg_name.get('content')
            except:
                pg_name = None
            try: 
                desc = card.find('meta', attrs={'itemprop': 'description'})
                desc = desc.get('content')
            except:
                desc = None

            charges = card.find('div', class_='m-srp-card__price').text.replace('₹', '')
            charges = charges.replace('\\n', '')
            charges = charges[0:8] + 'Onwards'

            try: 
                temp = card.find('span', attrs={'class': 'hidden'})
                posted_by = temp.get('data-advname')
                sharing_type = temp.get('data-avail').replace('\\', '')
                locality = temp.get('data-pglocality')
            except:
                pass
            entry=res_pg_model(Id=i, Posted_by=posted_by, PG_for=pg_for, Proptype='PG', Link=link, Owner=pg_name, City=city_opt, Locality=locality, Charges=charges, Description=desc)
            entry.save()
            i=i+1

def str_comm_sale_dt_db():   
   
    i=0

    for city_opt in cities:
        URL = "https://www.magicbricks.com/property-for-sale/commercial-real-estate?proptype=Commercial-Office-Space,Office-ITPark-SEZ,Commercial-Shop,Commercial-Showroom&cityName="+city_opt+"&language=en"
        for pgNo in range(0, 11):

            URL = URL+"&page="+str(pgNo)
            response = requests.get(URL)
            response = response.content
            soup = bs(response, 'html.parser')
            cards = soup.find_all('div', class_='mb-srp__card')
            print(len(cards))
            prop_age = 'Null'
            water = 'Null'
            carpet_area = 'Null'
            furnishing = 'Null'
            washroom = 'Null'
            parking = 'Null'
            pantry = 'Null'
            overlooking = 'Null'
            facing = 'Null'
            locality = 'Null'
            per_sqft = 'Null'
            desc = 'Null'
            date_posted = 'Null'

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
                    locality = city_opt
                childs = card.find('div', class_='mb-srp__card__summary-commercial__list--item')
                description = card.find('div', class_='mb-srp__card--desc')
                try: 
                    desc = description.find('p').text.replace('"', '')
                except:
                    desc = "Null"
                price = card.find('div', class_='mb-srp__card__price--amount').text.replace('₹', '')
                try: 
                    per_sqft = card.find('div', class_='mb-srp__card__price--size').text.replace('₹', '')
                except:
                    per_sqft = 'Null'
                for elem in childs:
                    try:
                        if 'Carpet Area' in elem.text:
                            carpet_area = elem.text.replace('Carpet Area', '')
                    except:
                        carpet_area = 'Null'

                    try:
                        if 'Overlooking' in elem.text:
                            overlooking = elem.text.replace('Overlooking', '')
                    except:
                        overlooking = 'Null'

                    try:
                        if 'Furnishing Status' in elem.text:
                            furnishing = elem.text.replace('Furnishing Status', '')
                    except:
                        furnishing = 'Null'

                    try:
                        if 'Parking' in elem.text:
                            parking = elem.text.replace('Parking', '')
                    except:
                        parking = 'Null'

                    try:
                        if 'Pantry' in elem.text:
                            pantry = elem.text.replace('Pantry', '')
                    except:
                        pantry = 'Null'

                    try:
                        if 'Facing' in elem.text:
                            facing = elem.text.replace('Facing', '')
                    except:
                        facing = 'Null'

                    try:
                        if 'Water Availability' in elem.text:
                            water = elem.text.replace('Water Availability', '')
                    except:
                        water = 'Null'

                    try:
                        if 'Property Age' in elem.text:
                            prop_age = elem.text.replace('Property Age', '')
                    except:
                        prop_age = 'Null'
                entry=comm_sale_model(Id=i, Date_Posted=date_posted, Proptype='Commercial Sale', Link=link, Owner=owner, Locality=locality, City=city_opt, Price=price, Carpet_Area=carpet_area, Facing=facing, Property_Age=prop_age, Water_Availability=water, Parking=parking, Pantry=pantry, Overlooking=overlooking, Description=desc)
                entry.save()
                i=i+1
    
        

def str_comm_lease_dt_db():
    i=0

    for city_opt in cities:
        print("entry");
        URL ="https://www.magicbricks.com/property-for-rent/commercial-real-estate?proptype=Commercial-Office-Space,Office-ITPark-SEZ,Commercial-Shop,Commercial-Showroom&cityName="+city_opt+"&language=en"
        for pgNo in range(0, 4):
            URL = URL+"&page="+str(pgNo)
            response = requests.get(URL)
            response = response.content
            soup = bs(response, 'html.parser')
            cards = soup.find_all('div', class_='mb-srp__card')
            print(len(cards));
            prop_age = "Null"
            water = "Null"
            carpet_area = "Null"
            ready_state = "Null"
            furnishing = "Null"
            washroom = "Null"
            parking = "Null"
            pantry = "Null"
            overlooking = "Null"
            facing = "Null"
            locality = "Null"
            per_sqft = "Null"
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
                    locality = city_opt
                childs = card.find_all('div', class_='mb-srp__card__summary-commercial__list--item')
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
                for elem in childs:

                    try:
                        if 'Carpet Area' in elem.text:
                            carpet_area = elem.text.replace('Carpet Area', '')
                    except:
                        carpet_area = "Null"

                    try:
                        if 'Overlooking' in elem.text:
                            overlooking = elem.text.replace('Overlooking', '')
                    except:
                        overlooking = "Null"

                    try:
                        if 'Furnishing Status' in elem.text:
                            furnishing = elem.text.replace('Furnishing Status', '')
                    except:
                        furnishing = "Null"

                    try:
                        if 'Parking' in elem.text:
                            parking = elem.text.replace('Parking', '')
                    except:
                        parking = "Null"

                    try:
                        if 'Pantry' in elem.text:
                            pantry = elem.text.replace('Pantry', '')
                    except:
                        pantry = "Null"

                    try:
                        if 'Facing' in elem.text:
                            facing = elem.text.replace('Facing', '')
                    except:
                        facing = "Null"

                    try:
                        if 'Washroom' in elem.text:
                            washroom = elem.text.replace('Washroom', '')
                    except:
                        washroom = "Null"

                    try:
                        if 'Water Availability' in elem.text:
                            water = elem.text.replace('Water Availability', '')
                    except:
                        water = "Null"

                    try:
                        if 'Property Age' in elem.text:
                            prop_age = elem.text.replace('Property Age', '')
                    except:
                        prop_age = "Null"
                entry=comm_lease_model(Id=i, Date_Posted=date_posted, Proptype='Commercial Sale', Link=link, Retailer=owner, BHK=bhk, Locality=locality, City=city_opt, Price=price, Carpet_Area=carpet_area, Washroom=washroom, Facing=facing, Water_Availability=water, Property_Age=prop_age, Price_Sqft=per_sqft, Parking=parking, Pantry=pantry, Description=desc)
                entry.save()
                i=i+1
        
# classes to view the data 
# the corresponding function will scrap and populate the database as the url is hit
class resSaleViewSet(viewsets.ModelViewSet):
    str_sale_dt_db()
    queryset=res_sale_model.objects.all()
    serializer_class=resSaleSerializer

class resRentViewSet(viewsets.ModelViewSet):
    str_rent_dt_db()
    queryset=res_rent_model.objects.all()
    serializer_class=resRentSerializer

class resPgViewSet(viewsets.ModelViewSet):
    str_pg_dt_db()
    queryset=res_pg_model.objects.all()
    serializer_class=resPgSerializer

class commSaleViewSet(viewsets.ModelViewSet):
    str_comm_sale_dt_db()
    queryset=comm_sale_model.objects.all()
    serializer_class=commSaleSerializer

class commLeaseViewSet(viewsets.ModelViewSet):
    str_comm_lease_dt_db()
    queryset=comm_lease_model.objects.all()
    serializer_class=commLeaseSerializer


