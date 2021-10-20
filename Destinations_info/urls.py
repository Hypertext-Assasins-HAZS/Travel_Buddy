''' /Destinations_info/urls.py '''

from Destinations_info.views import *
#from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns=[
    url(r'Paris/',paris),
    url(r'Toronto/',toronto),
    
]