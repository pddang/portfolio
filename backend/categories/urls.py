from django.urls import path, include
from . import views

urlpatterns = [
    path('api/category/', views.CategoryCreate.as_view()),
]