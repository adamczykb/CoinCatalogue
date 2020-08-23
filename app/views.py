"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.db import connection
from .models import *
from django.contrib import admin

def home(request):
    cursor = connection.cursor()
    search = request.GET.get('search', '')
    cursor.execute("select * from app_moneta where lower(nazwa) like lower('%" +
                   search+"%') or lower(opis) like lower('%"+search+"%') ")

    wynik = cursor.fetchall()
    cursor.execute("select * from app_katalog")
    katalog = cursor.fetchall()
    if request.user.is_authenticated:
        return render(request, 'app/index.html',
                      {
                          'title': 'Strona główna',
                          'monety': wynik,
                          'katalog': katalog
                      }
                      )
    else:
        return render(request, 'app/login.html')


def katalog(request, id_kat):
    cursor = connection.cursor()
    search = request.GET.get('search', '')
    cursor.execute("select * from app_moneta where katalog_id = "+id_kat +
                   "and (lower(nazwa) like lower('%"+search+"%') or lower(opis) like lower('%"+search+"%')) ")

    wynik = cursor.fetchall()
    cursor.execute("select * from app_katalog")
    katalog = cursor.fetchall()
    if request.user.is_authenticated:
        return render(request, 'app/index.html',
                      {
                          'title': 'Strona główna',
                          'monety': wynik,
                          'katalog': katalog
                      }
                      )
    else:
        return render(request, 'app/login.html')


def moneta(request, id_mon):
    cursor = connection.cursor()
    cursor.execute("select * from app_katalog")
    katalog = cursor.fetchall()
    obj = Moneta.objects.get(pk=id_mon)
    panowanie = Krolowie.objects.get(pk=obj.panowanie_id)
    material = Material.objects.get(pk=obj.material_id)
    mennica = Mennica.objects.get(pk=obj.mennica_id)
    rzadkosc = Rzadkosc.objects.get(pk=obj.rzadkosc_id)
    stan = Stan.objects.get(pk=obj.stan_id)
    dynastia = Dynastie.objects.get(pk=panowanie.dynastia_id)
    if request.user.is_authenticated:
        return render(request, 'app/moneta.html',
                      {
                          'title': obj.nazwa,
                          'katalog': katalog,
                          'moneta': obj,
                          'panowanie': panowanie,
                          'material': material,
                          'mennica': mennica,
                          'rzadkosc': rzadkosc,
                          'stan': stan,
                          'dynastia': dynastia
                      }
                      )
    else:
        return render(request, 'app/login.html' )
