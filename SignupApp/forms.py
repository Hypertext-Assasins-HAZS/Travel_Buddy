from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime
from django.forms import widgets
from django.utils import timezone

class DateInput(forms.DateInput):
    input_type = 'date'

class UserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=45)
    last_name = forms.CharField(max_length=45)
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=45)
    last_name = forms.CharField(max_length=45)
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']  
        
class TMSUserForm(forms.ModelForm):
    
    class Meta:
        model = TMSUser
        fields = ['mobileno','gender','nationality','pic','dob']
        widgets = {
            'dob' : DateInput
        }