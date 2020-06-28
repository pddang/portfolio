from django.shortcuts import render

# Create your views here.
from .serializers import CategorySerializer
from rest_framework import generics
from .models import Category


class CategoryCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
