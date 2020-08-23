from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models he
from .models import *


@admin.register(Krolowie)
@admin.register(Moneta)
@admin.register(Dynastie)
@admin.register(Material)
@admin.register(Rzadkosc)
@admin.register(Stan)
@admin.register(Katalog)
@admin.register(Mennica)
class KrolowieAdmin(admin.ModelAdmin):
    pass
