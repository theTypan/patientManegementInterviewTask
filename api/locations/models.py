from django.db import models

from common.models import AbstractBase


class County(AbstractBase):
	name = models.CharField(max_length=255)
	
	def __str__(self):
		return self.name

	class Meta:
		app_label = 'locations'
		verbose_name_plural = 'counties'

class Subcounty(AbstractBase):
	name = models.CharField(max_length=255)
	county = models.ForeignKey(County, on_delete=models.CASCADE, related_name='subcounties')

	def __str__(self):
		return self.name

	class Meta:
		app_label = 'locations'
		verbose_name_plural = 'subcounties'

class Ward(AbstractBase):
	name = models.CharField(max_length=255)
	subcounty = models.ForeignKey(Subcounty, on_delete=models.CASCADE, related_name='wards')

	def __str__(self):
		return self.name

	class Meta:
		app_label = 'locations'

class Village(AbstractBase):
	name = models.CharField(max_length=255)
	ward = models.ForeignKey(Ward, on_delete=models.CASCADE, related_name='villages')

	def __str__(self):
		return self.name

	class Meta:
		app_label = 'locations'