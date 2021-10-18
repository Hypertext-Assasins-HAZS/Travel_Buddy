''' /Signup/models.py '''

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class TMSUser(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	mobileno = models.CharField(max_length=10)
	pic = models.ImageField(default='default.jpg',upload_to='profile_pics',blank=True)
	dob = models.DateField(default=timezone.now)
	verified = models.BooleanField(default=False)