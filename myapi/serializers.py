from .models import Entries
from rest_framework import serializers

class EntriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Entries
        fields=('id','Date_Posted',' Proptype','Link', 'Owner', 'bHK', 'Locality', 'city', 'Price', 'Carpet_Area', 'Furnishing', 'Bathrooms', 'Facing', 'Status', 'Transaction', 'Price_Sqft', 'Floor', 'Description')
