from django.contrib import admin

from .models import Department, Patient


class PatientAdmin(admin.ModelAdmin):
	list_display = ('user', 'department', 'enrollment_number', 
		'enrollment_date', 'discharged',)

	list_filter = ['enrollment_date', 'discharged', ]
	search_fields = ['user',]

admin.site.register(Patient, PatientAdmin)

class DepartmentAdmin(admin.ModelAdmin):
	list_display = ('name','is_deleted',)

	def get_queryset(self, request):
		qs = Department.all_objects
		if request.user.is_superuser:
			return qs

admin.site.register(Department, DepartmentAdmin)