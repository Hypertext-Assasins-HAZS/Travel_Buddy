''' /SignupApp/urls.py '''

from SignupApp.views import *

from django.urls import path

urlpatterns=[
	path('signup/',signup),	
	path('userUpdate/',user_profile_update,name='userUpdate'),	
	path('userDelete/',user_profile_delete,name='userDelete'),	
]