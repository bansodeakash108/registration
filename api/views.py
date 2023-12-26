from django.shortcuts import render
from rest_framework import viewsets
from api.models import api_model
from api.serializer import api_serializer

# Create your views here.


class api_MVS(viewsets.ModelViewSet):
    queryset=api_model.objects.all()
    serializer_class=api_serializer