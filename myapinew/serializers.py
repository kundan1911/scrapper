from myapinew.models import *
from rest_framework import serializers

#pip install rest_framework
# the framework is used to view the data stored in the database
class resSaleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=res_sale_model
        fields=('Id','Date_Posted','Proptype','Link', 'Owner', 'BHK', 'Locality', 'City', 'Price', 'Carpet_Area', 'Furnishing', 'Bathrooms', 'Facing', 'Status', 'Transaction', 'Price_Sqft', 'Floor', 'Description')
# Id=i, Date_Posted=date_posted, Proptype='sale', Link=link, Owner=owner, BHK=bhk, Locality=locality, City=city_opt, Price=price, Carpet_Area=carpet_area, Furnishing=furnishing, Bathrooms=bathrooms, Facing=facing, Status=status, Transaction=transaction, Price_Sqft=per_sqft, Floor=floor, Description=desc

class resRentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=res_rent_model
        fields=('Id', 'Date_Posted', 'Link', 'Proptype', 'Owner', 'BHK', 'Locality', 'City', 'Rent', 'Carpet_Area', 'Furnishing', 'Facing', 'Tenant', 'Floor', 'Description')


class resPgSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=res_pg_model
        fields=('Id', 'Posted_by', 'PG_for', 'Link', 'Owner', 'Locality', 'City', 'Proptype', 'Charges', 'Description')



class commSaleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=comm_sale_model
        fields=('Id', 'Date_Posted', 'Link', 'Owner', 'Carpet_Area', 'Locality', 'City', 'Proptype', 'Price', 'Parking', 'Facing', 'Pantry', 'Water_Availability', 'Property_Age', 'Overlooking', 'Description')



class commLeaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=comm_lease_model
        fields=('Id', 'Date_Posted', 'Link', 'Proptype', 'Retailer', 'BHK', 'Locality', 'City', 'Price', 'Carpet_Area', 'Washroom', 'Facing', 'Water_Availability', 'Pantry', 'Price_Sqft', 'Property_Age', 'Parking', 'Description')


class noBrokerRentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=no_broker_rent_model
        fields=('Id','Date_Posted', 'Link', 'Rent', 'EMI', 'Nearby', 'SQFT', 'Furnishing', 'Available_from', 'Prop_Type', 'Preferred_Tenants', 'Apt_Type', 'Parking', 'Bedrooms', 'Possesion_By', 'Balcony');


class noBrokerSaleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=no_broker_sale_model
        fields=('Id','Date_Posted', 'Link', 'Price', 'EMI', 'Nearby', 'SQFT', 'Facing', 'Bathrooms', 'Apt_Type', 'Apt_Name', 'Parking', 'Bedrooms', 'Possesion_By', 'Balcony', 'Power_Backup');



