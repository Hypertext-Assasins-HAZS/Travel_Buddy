from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf

def paris(request):
    request.session['temp'] = "xyz"
    return render(request, 'paris.html')

def toronto(request):
	request.session['temp'] = "xyz"
	return render(request,'toronto.html')

# Create your views here.
