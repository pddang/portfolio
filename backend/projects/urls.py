from django.urls import path, include
from . import views

urlpatterns = [
    path('api/project/', views.ProjectCreate.as_view()),
]