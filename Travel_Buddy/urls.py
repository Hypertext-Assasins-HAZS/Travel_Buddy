''' /loginmodule/urls.py '''

from Travel_Buddy.views import *
#from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns=[
    url(r'^home/',home),
    url(r'^login/',login),
    url(r'^logout/',logout),
    url(r'^auth/',auth_view),
    url(r'^destinations/',destinations),
    url(r'^profile/',profile),
    url(r'^package_detail/',package_detail),
]