from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    company_image = models.ImageField(upload_to='images/companies/')
    duties = models.TextField(null=True)
    startDate = models.DateField(auto_now=True)
    endDate = models.DateField(auto_now_add=True)





