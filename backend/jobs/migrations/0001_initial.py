# Generated by Django 3.0.7 on 2020-06-27 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('company_image', models.ImageField(upload_to='images/companies/')),
                ('duties', models.TextField(null=True)),
                ('startDate', models.DateField(auto_now=True)),
                ('endDate', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
