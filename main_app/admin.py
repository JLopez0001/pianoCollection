from django.contrib import admin
from .models import Piano, MaintenanceRecord, Performer

# Register your models here.
admin.site.register(Piano)
admin.site.register(MaintenanceRecord)
admin.site.register(Performer)