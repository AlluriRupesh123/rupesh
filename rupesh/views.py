from django.shortcuts import render
from rupesh.models import  rupi
from rest_framework import generics
from rupesh .serializer import  rupiSerializer

# Create your views here.
class list(generics.ListAPIView):
    queryset = rupi.objects.all()
    serializer_class = rupiSerializer


