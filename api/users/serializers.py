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
			'is_patient',
			'is_staff',
			'is_superuser',
			'is_active',
			'is_deleted',
			'date_joined',
			'next_of_kin'
		)

		read_only_fields = ('last_login', 'date_joined', 'deleted',)