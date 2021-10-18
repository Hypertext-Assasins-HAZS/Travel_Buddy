''' /Signup/views.py '''

from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import auth
from django.template.context_processors import csrf
from SignupApp.models import TMSUser
from django.contrib.auth.models import User
from django.db import IntegrityError
from .forms import *
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'



def mobile_isValid(s):
    Pattern = re.compile("(0|91)?[7-9][0-9]{9}")
    return Pattern.match(s)




def signup(request):
	registered = False
	user_form = UserForm()
	tmsUser_form = TMSUserForm()
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		tmsUser_form = TMSUserForm(request.POST,request.FILES)
		if tmsUser_form.is_valid() and user_form.is_valid():
			user_data = user_form.cleaned_data 
			tmsUser_data = tmsUser_form.cleaned_data
			if (mobile_isValid(tmsUser_data["mobileno"])):
				# u=User.objects.create_user(username=uname,password=pwd,email=emailid)
				# print(u)
				# u.TMSUser = TMSUser(user=u,mobileno=mno,pic=profile_pic)
				# u.TMSUser.save()
				# u.save()
				# return HttpResponseRedirect('/Travel_Buddy/login/')
				user_form_instance = user_form.save()
				user_form_instance.set_password(user_form_instance.password)
				user_form_instance.save()
				
				tmsUser_form_instance = tmsUser_form.save(commit=False)
				tmsUser_form_instance.user = user_form_instance
				tmsUser_form_instance.save()
				registered = True
				
				return render(request, 'login.html',{'success':'You have been registered successfully !\nPlease login to explore...'})
		else:
			user_form = UserForm()
			tmsUser_form = TMSUserForm()
	context = {'user_form':user_form, 'tmsUser_form':tmsUser_form, 'registered':registered}
	return render(request,'signup.html',context)