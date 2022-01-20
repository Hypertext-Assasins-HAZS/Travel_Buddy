''' /DocumentApp/urls.py '''

from DocumentApp.views import *
from django.urls import path


urlpatterns = [
    path('docAdd/', DocumentAdd),
    path('DocAddPage/',  DocAddPage,name='DocAddPage'),
    path('userDocs/', userDocsView, name='userDocs'),
    path('docDelete/',DocumentDelete, name='docDelete'),
]