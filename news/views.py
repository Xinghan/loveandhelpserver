from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.decorators import list_route
from .models import Entry
from .serializers import EntrySerializer

class EntryViewSet(viewsets.ModelViewSet):
    import pdb; pdb.set_trace()
    queryset = Entry.objects.order_by('created')
    serializer_class = EntrySerializer
    lookup_field = 'slug'
    
