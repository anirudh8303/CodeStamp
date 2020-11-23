from django.contrib import admin
from .models import Patient, Doctors, Disease, Pharmacy

# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctors)
admin.site.register(Disease)
admin.site.register(Pharmacy)
