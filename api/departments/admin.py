from django.contrib import admin

from .models import Department, DepartmentPatient

admin.site.register(Department)
admin.site.register(DepartmentPatient)