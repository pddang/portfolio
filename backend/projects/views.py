from django.shortcuts import render
from .serializers import ProjectSerializer
from rest_framework import generics
from .models import Project


class ProjectCreate(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


