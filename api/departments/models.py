from django.db import models

from common.models import AbstractBase
from users.models import User


class Department(AbstractBase):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

	class Meta:
		app_label = 'departments'


class Patient(AbstractBase):
	department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='patients')
	patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_patients')
	enrollment_date = models.DateTimeField()
	discharged = models.BooleanField(default=False)

	def __str__(self):
		return self.patient.full_name

	@property
	def enrollment_number(self):
		return self.id

	def save(self, *args, **kwargs):
		if self.discharged:
			self.patient.patient = False
		else:
			self.patient.patient = True
		self.patient.save()
		super().save(*args, **kwargs)
	

	class Meta:
		app_label = 'departments'