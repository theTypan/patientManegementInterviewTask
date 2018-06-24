from django.contrib import admin

from .models import County, Subcounty, Ward, Village

class VillageInline(admin.TabularInline):
	model = Village
	extra = 3

class WardAdmin(admin.ModelAdmin):
	inlines = [VillageInline]

class WardInline(admin.TabularInline):
	model = Ward
	extra = 3

class SubcountyAdmin(admin.ModelAdmin):
	inlines = [WardInline]

class SubcountyInline(admin.TabularInline):
	model = Subcounty
	extra = 3

class CountyAdmin(admin.ModelAdmin):
	inlines = [SubcountyInline]

admin.site.register(County, CountyAdmin)
admin.site.register(Subcounty, SubcountyAdmin)
admin.site.register(Ward, WardAdmin)