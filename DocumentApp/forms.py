from django.forms import ModelForm
from django import forms
from .models import Document
from django.forms import widgets
from django.utils.crypto import get_random_string

class DateInput(forms.DateInput):
    input_type = 'date'

class DocumentForm(ModelForm):

    class Meta:
        model = Document
        fields = ['docType','expDate','docImg','docId']
        widgets = {
            'expDate' : DateInput
        }
        docId = forms.CharField(
            required=True,
            widget = forms.HiddenInput(
                attrs={
                    'name': 'docId',
                    'value': get_random_string(length=6)
            
            })
        )