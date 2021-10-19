from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Document(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,)
    docType = models.CharField(max_length=45,null=True)
    verified = models.BooleanField(default=False)
    expDate = models.DateField(default=timezone.now)
    docImg = models.ImageField(default='docImg_default.png',upload_to='documents')