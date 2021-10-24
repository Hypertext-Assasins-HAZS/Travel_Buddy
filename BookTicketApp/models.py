''' /BookTicketApp/models.py '''

from django.db import models
from SignupApp.models import TMSUser
from django.contrib.auth.models import User
from django.utils import timezone
from SignupApp.models import countries


class PackageDetails(models.Model):
	
	#id is the primary key automatically added by django
	pCity = models.CharField(max_length=20,default="no location given")
	pCountry = models.CharField( blank=True, null=True,default='N.A.', max_length=4,choices=countries())
	pdetails = models.TextField(blank=True,max_length=200,default='no package details provided !')
	pic = models.ImageField(default='pdefault.jpg',upload_to='package_pics')
	amount = models.PositiveIntegerField(default=1000)
	def __str__(self):
		return f"{self.pCity}, {self.pCountry}"
	
	
class TMSBooking(models.Model):
	TYPES = [
        ('Common','Common'),
        ('Special','Special'),
        ('Luxury','Luxury'), 
	] 
	booking_id=models.CharField(max_length=6,primary_key=True)
	tmsuser = models.ForeignKey(TMSUser,on_delete=models.CASCADE,null=True)
	source = models.CharField(max_length=20)
	destinationCity = models.CharField(max_length=20)
	destinationCountry = models.CharField(max_length=20)
	package = models.ForeignKey(PackageDetails,on_delete=models.CASCADE,null=True)
	ptype = models.CharField(default='common',max_length=10,choices=TYPES)
	departure_date = models.DateField(blank=True,default=timezone.now)
	no_of_person = models.PositiveIntegerField(default=1)
	amount=models.PositiveIntegerField()
	
		


