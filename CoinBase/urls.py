"""
Definition of urls for CoinBase.
"""
from django.conf.urls import url, include
from datetime import datetime
from django.urls import path
import django.contrib.auth.views
from django.contrib import admin
import app.forms
import app.views
from django.conf import settings
from django.conf.urls.static import static
# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    path('', app.views.home, name='home'),
    path('katalog/<str:id_kat>', app.views.katalog, name='katalog'),
    path('moneta/<str:id_mon>', app.views.moneta, name='moneta'),
    path('admin/', admin.site.urls, name='admin'),
    path('accounts/', include('django.contrib.auth.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
