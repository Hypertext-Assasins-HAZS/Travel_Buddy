'''/PaymentApp/urls.py'''

from PaymentApp.views import *
from django.conf.urls import url
from django.urls import path

urlpatterns=[
	path('CalculateAmount/',CalculateAmount),
	path('makepayment/',makepayment),
	path('bill/',bill),
]