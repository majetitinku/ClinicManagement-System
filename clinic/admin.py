from django.contrib import admin
from .models import Patient, Staff, Appointment

admin.site.register(Patient)
admin.site.register(Staff)
admin.site.register(Appointment)