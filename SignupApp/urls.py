''' /Signup/urls.py '''

from SignupApp.views import *
from django.conf.urls import url
from django.urls import path

urlpatterns=[
	path('signup/',signup),
	
]