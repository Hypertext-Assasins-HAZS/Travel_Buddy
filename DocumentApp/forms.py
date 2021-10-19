from django.forms import ModelForm
from django import forms
from .models import Document
from django.forms import widgets

class DateInput(forms.DateInput):
    input_type = 'date'

class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ['docType','expDate','docImg']
        widgets = {
            'expDate' : DateInput
        }