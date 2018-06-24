from django.contrib import admin

from .models import Department, Patient

admin.site.register(Department)

class PatientAdmin(admin.ModelAdmin):
	list_display = ('user', 'department', 'enrollment_number', 
		'enrollment_date', 'discharged',)

	list_filter = ['enrollment_date', 'discharged', ]
	search_fields = ['user',]

admin.site.register(Patient, PatientAdmin)