from django.contrib import admin
from .models import Patient, Doctors, Disease, Pharmacy, Appointment

# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctors)
admin.site.register(Disease)
admin.site.register(Pharmacy)
admin.site.register(Appointment)
