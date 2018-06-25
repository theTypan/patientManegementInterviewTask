from django.db import models
from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager, PermissionsMixin	
	)
from django.utils import timezone

import uuid

from phonenumber_field.modelfields import PhoneNumberField

from locations.models import County, Subcounty, Ward, Village

from common.models import SoftDeletionModel

GENDER_CHOICES = (
	('M', 'Male'),
	('F', 'Female'),
	)

class UserManager(BaseUserManager):
	"""
	Custom user manager.
	"""
	def create_user(self, email, first_name, password=None):
		"""
		Creates and saves a User with the given email, first name and password.
		"""
		if not email:
			raise ValueError('Email is required for a user')

		if not first_name:
			raise ValueError('First name is required for a user')

		if not password:
			raise ValueError('Password is required for a user')

		user = self.model(
			email = self.normalize_email(email)
		)
		user.set_password(password)
		user.first_name = first_name
		user.save(using=self._db)
		return user

	def create_patient(self, email, first_name, password):
		""""
		Creates and saves a patient user with the given email, first name
		and password.
		"""
		user = self.create_user(email, first_name, password)
		user.is_patient = True
		user.save(using=self._db)
		return user

	def create_staff(self, email, first_name, password):
		"""
		Creates and saves a staff user with the given email, first name
		and password.
		"""
		user = self.create_user(email, first_name, password)
		user.is_staff = True
		user.save(using=self._db)
		return user

	def create_superuser(self, email, first_name, password):
		"""
		Creates and saves a superuser with the given email, first name
		and password.
		"""
		user = self.create_user(email, first_name, password)
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class User(AbstractBaseUser, PermissionsMixin, SoftDeletionModel):
	""" 
	Custom user class. 
	"""

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name']

	objects = UserManager()

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255, null=True, blank=True)
	other_names = models.CharField(max_length=255, null=True, blank=True)
	primary_phone_number = PhoneNumberField(unique=True)
	alternative_phone_number = PhoneNumberField(blank=True, null=True)
	email = models.EmailField(unique=True)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
	date_of_birth = models.DateField(null=True, blank=True)
	county = models.ForeignKey(County, on_delete=models.CASCADE, null=True, blank=True)
	subcounty = models.ForeignKey(Subcounty, on_delete=models.CASCADE, null=True, blank=True)
	ward = models.ForeignKey(Ward, on_delete=models.CASCADE, null=True, blank=True)
	village = models.ForeignKey(Village, on_delete=models.CASCADE, null=True, blank=True)
	next_of_kin = models.ManyToManyField('User', blank=True)
	is_patient = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	date_joined = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.email

	def full_name(self):
		"""
		Returns a user's first name plus the last name if last name available or 
		first name plus last name and other names if last name and other names
		available seprated by spaces
		"""
		full_name = '%s %s %s' % (self.first_name, (self.last_name or ''), (self.other_names or ''))

		return ' '.join(full_name.split())

	def short_name(self):
		"""
		Returns the first name of a user
		"""
		return self.first_name