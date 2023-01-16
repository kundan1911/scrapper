from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EntriesSerializer
from .models import Entries
# Create your views here.

class EntryViewSet(viewsets.ModelViewSet):
    queryset=Entries.objects.all()
    serializer_class=EntriesSerializer
