from .models import Entries
from rest_framework import serializers

class EntriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Entries
        fields=('Id', 'Date_Posted', 'Link', 'Proptype', 'Owner', 'bHK', 'Locality', 'City', 'Price', 'Carpet_Area', 'Furnishing', 'Bathrooms', 'Facing', 'Status', 'Transaction', 'Price_Sqft', 'Floor', 'Description')
