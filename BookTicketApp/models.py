''' /BookTicketApp/models.py '''

from django.db import models
from SignupApp.models import TMSUser
from django.contrib.auth.models import User
from django.utils import timezone
from SignupApp.models import countries


class PackageDetails(models.Model):
	TYPES = [
        ('common','Common'),
        ('special','Special'),
        ('luxury','Luxury'), 
	] 
	pname = models.CharField(max_length=20,primary_key=True)
	pdestination = models.CharField(max_length=20,default="no location given")
	pCountry = models.CharField( blank=True, null=True,default='N.A.', max_length=4,choices=countries())
	pdetails = models.TextField(blank=True,max_length=200,default='no package details provided !')
	pic = models.ImageField(default='pdefault.jpg',upload_to='package_pics')
	amount = models.CharField(default='1000',max_length=5)
	ptype = models.CharField(default='common',max_length=10,choices=TYPES)
	
class TMSBooking(models.Model):
	booking_id=models.CharField(max_length=6,primary_key=True)
	tmsuser = models.ForeignKey(TMSUser,on_delete=models.CASCADE,null=True)
	source = models.CharField(max_length=20)
	destination = models.CharField(max_length=20)
	package = models.ForeignKey(PackageDetails,on_delete=models.CASCADE,null=True)
	departure_date = models.DateField(blank=True,default=timezone.now)
	no_of_person = models.PositiveIntegerField(default=1)
	amount=models.PositiveIntegerField()

class feedback(models.Model):
	
	tmsuser = models.ForeignKey(TMSUser, on_delete=models.CASCADE, null=True)
	feedback=models.TextField(max_length=200)
