from django.contrib import admin
from .models import Piano, MaintenanceRecord

# Register your models here.
admin.site.register(Piano)
admin.site.register(MaintenanceRecord)