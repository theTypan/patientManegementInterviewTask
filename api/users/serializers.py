from rest_framework import serializers

from  users.models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = (
			'id',
			'first_name',
			'last_name',
			'other_names',
			'primary_phone_number',
			'alternative_phone_number',
			'email',
			'gender',
			'date_of_birth',
			'county',
			'subcounty',
			'ward',
			'village',
			'patient',
			'staff',
			'superuser',
			'active',
			'deleted',
			'date_joined',
		)

		read_only_fields = ('last_login', 'date_joined', 'deleted',)