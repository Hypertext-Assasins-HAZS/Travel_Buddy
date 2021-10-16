''' /DocumentApp/urls.py '''

from DocumentApp.views import *
from django.conf.urls import url
from django.urls import path


urlpatterns = [
    path('docAdd/', DocumentAdd),
]