from django.contrib import admin
from .models import bom1


class bom1Admin(admin.ModelAdmin):
    search_fields = ['jepum_code']


admin.site.register(bom1, bom1Admin)

