from django.contrib import admin

from .models import Department, Patient

admin.site.register(Department)
admin.site.register(Patient)