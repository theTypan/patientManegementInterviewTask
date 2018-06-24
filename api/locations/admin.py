from django.contrib import admin

from .models import County, Subcounty, Ward, Village

admin.site.register(County)
admin.site.register(Subcounty)
admin.site.register(Ward)
admin.site.register(Village)