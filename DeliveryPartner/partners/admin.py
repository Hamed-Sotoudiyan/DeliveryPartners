# from django.contrib import admin
from django.contrib.gis import admin

from .models import Partner
# Register your models here.
class PartnerAdmin(admin.GeoModelAdmin):
    list_display = ['id']

admin.site.register(Partner,PartnerAdmin)