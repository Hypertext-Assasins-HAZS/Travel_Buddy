''' /PaymentApp/views.py '''

from django.shortcuts import render
from django.template.context_processors import csrf
from BookTicketApp.models import PackageDetails,TMSBooking
from django.contrib.auth.decorators import login_required
from SignupApp.models import TMSUser
from BookTicketApp.models import PackageDetails,TMSBooking
from .models import TMSPayment
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.http import HttpResponseRedirect
from django.utils.crypto import get_random_string

@login_required
def CalculateAmount(request):
    return render(request,'amountnew.html')

@login_required
def bill(request):
    if request.method == 'POST':
        c={}
        paymentId=get_random_string(length=6)
        modeOfPayment=request.POST.get('mode')
       
        total_amount=request.session['total_amount_rs']
        bookingid=request.session['booking_id']
        print(bookingid)
        pckg=request.session['package']
        no_of_person=request.session['nop']
        source1=request.session['source']
        city=request.session['destinationCity']
        country=request.session['destinationCountry']
        date=request.session['date']
        ptype=request.session['package_type']
        request.session['payId']= paymentId
        request.session['paymentMode'] = modeOfPayment
        
        p=TMSPayment(payment_id=paymentId,amount=total_amount,mode=modeOfPayment,tmsuser=TMSUser.objects.get(user=request.user))
        
        s=TMSBooking(booking_id=bookingid,amount=total_amount,source=source1,destinationCity=city,destinationCountry=country,
        			package=PackageDetails.objects.get(id=pckg),departure_date=date,
        			no_of_person=no_of_person,tmsuser=TMSUser.objects.get(user=request.user))
        p.save()
        s.save()
        return render(request,'billnew.html',c)
    else:
        return render(request,'amountnew.html')