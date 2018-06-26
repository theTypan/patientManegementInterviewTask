from django.contrib.auth import get_user_model
User = get_user_model()


class PhoneNumberBackend(object):
	def authenticate(self, username=None, password=None, **kwargs):
		try:
			user = User.objects.get(primary_phone_number=username)

		except User.MultipleObjectsReturned:
			user = User.objects.filter(primary_phone_number=username).order_by('id').first()
		except User.DoesNotExist:
			return None

		if getattr(user, 'is_active') and user.check_password(password):
			return user
		return None

	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
		except User.UserDoesNotExist:
			return None