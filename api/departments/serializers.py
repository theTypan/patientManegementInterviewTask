from rest_framework import serializers

from departments.models import Department, DepartmentPatient
from users.serializers import UserSerializer

class DepartmentPatientSerializer(serializers.ModelSerializer):
	patient = UserSerializer()

	class Meta:
		model = DepartmentPatient
		fields = (
			'enrollment_number',
			'department',
			'patient',
			'enrollment_date',
		)

class DepartmentSerializer(serializers.ModelSerializer):
	patients = DepartmentPatientSerializer(many=True, read_only=True)

	class Meta:
		model = Department
		fields = (
			'id',
			'name',
			'patients'
		)

