''' /Travel_Buddy/urls.py '''

from Travel_Buddy.views import *
#from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.urls import path

urlpatterns=[
    path('home/',home),
    path('login/',login),
    path('logout/',logout),
    path('auth/',auth_view),
    path('destinations/',destinations),
    path('profile/',profile),
    path('package_detail/',package_detail),
]