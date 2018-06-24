from django.db import models
from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager, PermissionsMixin	
	)
from django.utils import timezone

import uuid

from phonenumber_field.modelfields import PhoneNumberField

from locations.models import County, Subcounty, Ward, Village

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
		user.patient = True
		user.save(using=self._db)
		return user

	def create_staff(self, email, first_name, password):
		"""
		Creates and saves a staff user with the given email, first name
		and password.
		"""
		user = self.create_user(email, first_name, password)
		user.staff = True
		user.save(using=self._db)
		return user

	def create_superuser(self, email, first_name, password):
		"""
		Creates and saves a superuser with the given email, first name
		and password.
		"""
		user = self.create_user(email, first_name, password)
		user.staff = True
		user.superuser = True
		user.save(using=self._db)
		return user


class User(AbstractBaseUser, PermissionsMixin):
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
	primary_phone_number = PhoneNumberField(unique=True, blank=True, null=True)
	alternative_phone_number = PhoneNumberField(unique=True, blank=True, null=True)
	email = models.EmailField(unique=True)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
	date_of_birth = models.DateField(null=True, blank=True)
	county = models.ForeignKey(County, on_delete=models.CASCADE, null=True)
	subcounty = models.ForeignKey(Subcounty, on_delete=models.CASCADE, null=True)
	ward = models.ForeignKey(Ward, on_delete=models.CASCADE, null=True)
	village = models.ForeignKey(Village, on_delete=models.CASCADE, null=True)
	patient = models.BooleanField(default=False)
	staff = models.BooleanField(default=False)
	superuser = models.BooleanField(default=False)
	active = models.BooleanField(default=True)
	deleted = models.BooleanField(default=False)
	date_joined = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return "{}".format(self.full_name)

	@property
	def full_name(self):
		"""
		Returns a user's first name plus the last name if last name available or 
		first name plus last name and other names if last name and other names
		available seprated by spaces
		"""
		full_name = '%s %s %s' % (self.first_name, (self.last_name or ''), (self.other_names or ''))

		return ' '.join(full_name.split())

	@property
	def short_name(self):
		"""
		Returns the first name of a user
		"""
		return self.first_name

	@property
	def is_patient(self):
		"""
		Return True if a user is a patient, False otherwise
		"""
		return self.patient

	@property
	def is_staff(self):
		"""
		Return True if a user is an an staff, False otherwise
		"""
		return self.staff

	@property
	def is_superuser(self):
		"""
		Return True if a user is a superuser, False otherwise
		"""
		return self.superuser

	@property
	def is_active(self):
		"""
		Return True if a user account is active, False otherwise
		"""
		return self.active

	@property
	def is_deleted(self):
		"""
		Returns True if a user account is deleted, False otherwise
		"""
		return self.deleted

	def delete(self, *args, **kwargs):
		"""
		Mark the User field deleted true
		"""
		self.deleted = True
		self.active = False
		self.save()

	def enroll(self, *args, **kwargs):
		"""
		Mark the User field patient true
		"""
		self.patient = True
		self.save()

	def unenroll(self, *args, **kwargs):
		"""
		Mark the User field patient false
		"""
		self.patient = False
		self.save()

