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
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='patients')
	enrollment_date = models.DateTimeField()
	discharged = models.BooleanField(default=False)

	def __str__(self):
		return self.user.email

	def enrollment_number(self):
		return self.id

	def save(self, *args, **kwargs):
		if self.discharged:
			self.user.is_patient = False
		else:
			self.user.is_patient = True
		self.user.save()
		super().save(*args, **kwargs)
	

	class Meta:
		app_label = 'departments'