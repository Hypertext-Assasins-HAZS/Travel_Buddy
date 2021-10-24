''' myTMS/urls.py(project's urls.py) '''

from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
from Travel_Buddy.views import home
from django.conf import settings
from django.conf.urls.static import static


from django.views.generic import RedirectView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/Travel_Buddy/index/')),
    path('Travel_Buddy/', include('Travel_Buddy.urls')),
    path('SignupApp/', include('SignupApp.urls')),
    path('BookTicketApp/', include('BookTicketApp.urls')),
    path('PaymentApp/', include('PaymentApp.urls')),
    path('DocumentApp/', include('DocumentApp.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)