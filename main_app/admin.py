from django.contrib import admin

# Register your models here.
from .models import Sandwich, Ingredient

admin.site.register(Sandwich)
admin.site.register(Ingredient)