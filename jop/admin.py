from django.contrib import admin

# Register your models here.

from .models import Jop, Category

admin.site.register(Jop)
admin.site.register(Category)