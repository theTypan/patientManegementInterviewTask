from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
	list_display = ('email', 'primary_phone_number', 'is_patient', 
		'is_staff', 'is_active', 'is_superuser', 'is_deleted')
	list_filter = ['date_joined', 'patient', ]
	search_fields = ['email', 'primary_phone_number',]

admin.site.register(User, UserAdmin)