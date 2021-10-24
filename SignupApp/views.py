''' /Signup/views.py '''

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.template.context_processors import csrf
from SignupApp.models import TMSUser
from django.contrib.auth.models import User
from django.db import IntegrityError
from .forms import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
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
		tmsUser_form = TMSUserForm(request.POST,request.FILES) #check enctype in htmlform to get files
		if tmsUser_form.is_valid() and user_form.is_valid():
			user_form_instance = user_form.save(commit=False)
			user_form_instance.set_password(user_form.cleaned_data['password1'])  #####bug found 
			user_form_instance.save()
			tmsUser_form_instance = tmsUser_form.save(commit=False)
			tmsUser_form_instance.user = user_form_instance
			tmsUser_form_instance.save()
			registered = True

			# return render(request, 'login.html',{'success':'You have been registered successfully !\nPlease login to explore...'})
			return HttpResponseRedirect(reverse('login'))
	else:
		user_form = UserForm()
		tmsUser_form = TMSUserForm()
	print((request.FILES.get('pic')))
	context = {'user_form':user_form, 'tmsUser_form':tmsUser_form, 'registered':registered}
	return render(request,'signup.html',context)


@login_required
def user_profile_update(request):
	c={}
	if request.method == 'POST':
		user_update_form = UserUpdateForm(request.POST,instance=request.user)
		tmsUser_update_form = TMSUserForm(request.POST,request.FILES,instance=request.user.tmsuser)
		if user_update_form.is_valid() and tmsUser_update_form.is_valid():
			user_update_form_instance = user_update_form.save()   
			tmsUser_update_form_instance = tmsUser_update_form.save(commit=False)
			tmsUser_update_form_instance.user = request.user
			tmsUser_update_form_instance.save()
			username = user_update_form.cleaned_data.get('username')
			c['success']=f'Your account was successfully updated {request.user.username}'
			# return HttpResponseRedirect(reverse('userUpdate'))
			return render(request, 'userUpdate.html',c)
		else:
			c['success']='Could not update....some error occured'
			return HttpResponseRedirect(reverse('signup'))
	else:
		user_update_form = UserUpdateForm(instance=request.user)
		tmsUser_update_form = TMSUserForm(instance=request.user.tmsuser)
	context = {
		'user_update_form':user_update_form,
		'tmsUser_update_form':tmsUser_update_form,
	}
	return render(request, 'userUpdate.html', context=context)

@login_required
def user_profile_delete(request):
	if request.method == 'POST':
		User.objects.filter(username=request.user.username).delete()
		return HttpResponseRedirect(reverse('home'))
	else:
		return HttpResponseRedirect(reverse('profile'))

