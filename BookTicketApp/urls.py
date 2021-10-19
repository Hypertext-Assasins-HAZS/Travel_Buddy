''' /BookTicketApp/urls.py '''

from BookTicketApp.views import *
from django.conf.urls import url
from django.urls import path


urlpatterns=[
	path('book_ticket/',book_ticket),
	path('bookingdataadd/',bookingdataadd),
	path('booking_history/', booking_history),
	path('delete/',delete),
	path('feedback/',feedback),

]