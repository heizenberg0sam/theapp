from email.headerregistry import Address
from django.db import models
from operator import truediv
from tkinter import CASCADE
from unicodedata import name
from venv import create
from django.db import models
from django.contrib.auth.models import User







class lawyer(models.Model):
    data = models.CharField(max_length=300)
    name =  models.CharField(max_length=200)
    phonenum = models.CharField(max_length=50)
    areasop = models.TextField(null=True, blank = True)
    consuls = models.IntegerField(null=True)    
    created = models.DateTimeField(auto_now_add=True)
    bio = models.TextField(null=True, blank = True)
    #address = models.TextField(null=True, blank = True)


    class Meta:
        verbose_name_plural="وکلا"

    def __str__(self):
        return self.name


class OrderNow(models.Model):
    name=models.CharField(max_length=200)
    phonenum = models.CharField(max_length=50)
    user = models.ForeignKey(User , on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank = True)
    time = models.TimeField(null=True,blank = True)
    chosenlawyer = models.ForeignKey(lawyer , on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    is_fulfilled = models.BooleanField(default=False)
    

    class Meta:
        verbose_name_plural="سفارشات"

    def __str__(self):
        return self.name
  


