from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings



DOC_TYPES = [
        ('Passport','Passport'),
        ('Adhar','Adhar'),
        ('voter-Id','Voter-Id'),
        ('pan-card','PAN Card'),
        ('driving-licencse','Driving-licencse'), 
        ('Flight-ticket','Flight-Ticket'),
        ('Hotel-reservation','Hotel-Reservation'),
        ('Other-document','Other'),
	] 
# Create your models here.
class Document(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,)
    docType = models.CharField(max_length=45,null=True,choices=DOC_TYPES)
    verified = models.BooleanField(default=False)
    expDate = models.DateField(default=timezone.now)
    docImg = models.FileField(default='docImg_default.png',upload_to='documents')