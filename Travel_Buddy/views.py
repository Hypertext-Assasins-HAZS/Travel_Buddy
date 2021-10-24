''' /Travel_Buddy/views.py '''

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.template.context_processors import csrf
from BookTicketApp.models import PackageDetails





# print(countrie_name("WF"))

def home(request):
	# print(request.user.tmsuser.pic.url)

	c={}
	c.update(csrf(request))
	request.session['temp'] = "xyz"
	c['packs'] = PackageDetails.objects.all()
	return render(request,'home.html',c)

def user_login(request):
	if request.method == 'POST':
		print("inside")
		username = request.POST['username']   ##don't use get method...
		password = request.POST['password']  ##don't use get method...
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/Travel_Buddy/home')
			else:
				return render(request,'login.html',{"error":"Account not active !"})
		else:
				print("someone tried to login but failed !")
				print("Username : {} and Password {} ".format(username, password))
				return render(request,'login.html',{"error":"Invalid Username or Password !"})
	else:
		c={}
		return render(request,'login.html',c)


def user_logout(request):
	logout(request)
	return render(request, 'logout.html')

def aboutus(request):
	request.session['temp'] = "xyz"
	return render(request,'aboutus.html')

def profile(request):
	request.session['temp'] = "xyz"
	return render(request,'profile.html')

def package_detail(request):
	request.session['temp'] = "xyz"
	return render(request,'package_detail.html')

def destinationsView(request):
    # print(dir(PackageDetails))
    
    destinations = PackageDetails.objects.all()
    
    c={
        'destinations':destinations,
        
    }
    
    request.session['temp'] = "xyz"
    return render(request,'destinations.html',c)
     
def index(request):
	request.session['temp'] = "xyz"
	return render(request,'index.html')


