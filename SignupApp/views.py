''' /Signup/views.py '''

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from SignupApp.models import TMSUser
from django.contrib.auth.models import User
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'



def mobile_isValid(s):
    Pattern = re.compile("(0|91)?[7-9][0-9]{9}")
    return Pattern.match(s)



def signup(request):
    c={}
    c.update(csrf(request))
    return render(request,'signup.html',c)

def adduserinfo(request):
	if request.method == 'POST':
		uname=request.POST.get('username','')
		pwd=request.POST.get('password','')
		cpwd=request.POST.get('cpassword','')
		emailid=request.POST.get('emailid','')
		mno=request.POST.get('mobileno','')
		profile_pic = request.FILES['profile_pic']
		if(pwd==cpwd):
			if(len(pwd)>=8):
				if(mobile_isValid(mno)):
					if(re.fullmatch(regex, emailid)):
		
						u=User.objects.create_user(username=uname,password=pwd,email=emailid)
						print(u)
						u.TMSUser = TMSUser(user=u,mobileno=mno,pic=profile_pic)
						u.TMSUser.save()
						u.save()
						return HttpResponseRedirect('/Travel_Buddy/login/')
					else:
						return render(request,'signup.html',{"error4":"Email is invalid"})
				else:
					return render(request,'signup.html',{"error3":"Mobile no is invalid"})
			else:
				return render(request,'signup.html',{"error1":"Password length is lessthan 8"})
		else:
			return render(request,'signup.html',{"error2":"Password doesn't match enter again"})