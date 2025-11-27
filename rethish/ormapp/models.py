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

