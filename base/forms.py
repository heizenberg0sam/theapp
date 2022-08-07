from dataclasses import fields
from msilib.schema import Class
from django.forms import HiddenInput, ModelForm  #different formsssssss checkt hem out
from .models import OrderNow , lawyer 
from django.contrib.auth.models import User


class OrderForm(ModelForm):
     class Meta:
       model = OrderNow          #magically makes the form!!!
       fields= '__all__'      #what Room needs to be filled
       exclude = ['user' , 'is_fulfilled']

class LawyerForm(ModelForm):
     class Meta:
       model = lawyer          #magically makes the form!!!
       fields= '__all__'      #what Room needs to be filled
       

class UserForm(ModelForm):
  class Meta:
    model = User
    fields = ['username','email','first_name','last_name']
