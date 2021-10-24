''' /BookTicketApp/admin.py '''

from django.contrib import admin
from .models import PackageDetails,TMSBooking

admin.site.register(PackageDetails)
admin.site.register(TMSBooking)