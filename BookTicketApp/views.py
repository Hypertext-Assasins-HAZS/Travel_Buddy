''' /BookTicketApp/views.py '''
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from BookTicketApp.models import TMSBooking,PackageDetails
from SignupApp.models import TMSUser
from PaymentApp.models import TMSPayment
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils.crypto import get_random_string
from django.utils.timezone import datetime

def final_price(amt,ptype):
	amt=int(amt)
	if ptype == 'Special':
		amt = amt*1.1
		return amt
	elif ptype == 'Luxury':
		amt = amt*1.2
		return amt
	else:
		return amt
	

@login_required
def book_ticket(request):
	s=TMSBooking.objects.filter()
	c={}
	c.update(csrf(request))
	request.session['temp']="xyz"
	request.session['full_name']=request.user.username
	c['packages'] = PackageDetails.objects.all()
	c['randomid']=get_random_string(length=6)
	return render(request,'book_ticketnew.html',c)


@login_required
def bookingdataadd(request):
	c = {}
	bookingid=request.POST.get('bookingid')
	source1=request.POST.get('source')
	pckg=request.POST.get('destination') #select option returns id of package
	print(bookingid)
	ptype=request.POST.get('radio')
	date=request.POST.get('date')
	no_of_person=request.POST.get('person')
	country = amt=PackageDetails.objects.get(id=pckg).pCountry
	city = amt=PackageDetails.objects.get(id=pckg).pCity
	
	amt=PackageDetails.objects.get(id=pckg).amount
	pamt_after_type = final_price(amt,ptype)
	total_amount=int(no_of_person)*int(pamt_after_type)
	c['total_amount']=total_amount

	#dictionary to pass all the above values to payment app:
	# s=TMSBooking(booking_id=bookingid,amount=total_amount,source=source1,destinationCity=city,destinationCountry=country,
	# 			 package=PackageDetails(id=pckg),departure_date=date,
	# 			 no_of_person=no_of_person,tmsuser=TMSUser.objects.get(user=request.user))
	if(source1!=country):
		# s.save()
		###using request.session you can pass all these value in other html pages.##
		request.session['total_amount_rs'] = total_amount
		request.session['booking_id']= bookingid
		request.session['package']=pckg
		request.session['nop'] = no_of_person
		request.session['source']=source1
		request.session['destinationCity']=city
		request.session['destinationCountry']=country
		request.session['date']=date
		request.session['package_type']=ptype
		request.session['test']='xyz'
		
		return render(request,'amountnew.html',c)
	else:
		request.session['error']="Source and Destination can't be same"
		return HttpResponseRedirect('/BookTicketApp/book_ticket/')


@login_required
def booking_history(request):

	request.session['temp']="abc"
	c={}
	c['today']=datetime.today().date()
	c['bookings'] = TMSBooking.objects.filter(tmsuser=request.user.tmsuser)
	c['payments'] = TMSPayment.objects.filter(tmsuser=request.user.tmsuser)
	return render(request,'booking_history.html',c)

def delete(request):
	TMSBooking.objects.filter(booking_id=request.POST.get('cancel')).delete()
	return HttpResponseRedirect('/BookTicketApp/booking_history/')


