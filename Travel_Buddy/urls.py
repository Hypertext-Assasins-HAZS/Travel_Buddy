''' /Travel_Buddy/urls.py '''

from Travel_Buddy.views import *
#from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.urls import path

urlpatterns=[
    path('home/',home),
    path('index/',index),
    path('login/',user_login),
    path('logout/',user_logout),
    path('destinations/',destinationsView),
    path('profile/',profile),
    path('package_detail/',package_detail),
]