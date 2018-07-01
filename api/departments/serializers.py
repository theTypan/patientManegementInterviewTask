from rest_framework import serializers

from departments.models import Department, Patient
from users.serializers import UserSerializer

class PatientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Patient
		fields = (
			'enrollment_number',
			'user',
			'department',
			'enrollment_date',
			'discharged',
		)

class DepartmentSerializer(serializers.ModelSerializer):
	patients = PatientSerializer(many=True, read_only=True)

	class Meta:
		model = Department
		fields = (
			'id',
			'name',
			'patients',
		)

