# Ex01 Django ORM Web Application
## Date: 
27-11-2025
## AIM
To develop a Django Application to store and retrieve data from a E-Commerce Website Database for Amazon or Flipkart using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
## MODEL:
```
from django.db import models
from django.contrib import admin
class pr(models.Model):
    pid=models.CharField(primary_key=True,max_length=8)
    pName=models.CharField(max_length=30)
    cost=models.FloatField()
    creview=models.FloatField()
    Deliverydate=models.DateTimeField()
    company=models.CharField(max_length=20)
    quantity=models.IntegerField()
    
class prAdmin(admin.ModelAdmin):
    list_display=["pid","pName","cost","creview","Deliverydate","company","quantity"]

```
## ADMIN:
```
from django.contrib import admin
from .models import pr,prAdmin
admin.site.register(pr,prAdmin)
```

## OUTPUT

![alt text](<Screenshot (16).png>)

## RESULT
Thus the program for creating Product database using ORM hass been executed successfully
