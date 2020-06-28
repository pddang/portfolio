from django.db import models

from categories.models import Category


class Project(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name="category", on_delete=models.CASCADE)
    description = models.TextField(null=True)
    tools = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


