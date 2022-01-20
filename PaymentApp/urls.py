'''/PaymentApp/urls.py'''

from PaymentApp.views import *

from django.urls import path

urlpatterns=[
	path('CalculateAmount/',CalculateAmount),
	path('bill/',bill),
]