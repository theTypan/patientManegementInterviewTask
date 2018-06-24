from rest_framework import serializers

from  locations.models import County, Subcounty, Ward, Village


class VillageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Village
		fields = (
			'id',
			'name',
			'ward',
		)

class WardSerializer(serializers.ModelSerializer):
	villages = VillageSerializer(many=True, read_only=True)

	class Meta:
		model = Ward
		fields = (
			'id',
			'name',
			'subcounty',
			'villages',
		)

class SubcountySerializer(serializers.ModelSerializer):
	wards = WardSerializer(many=True, read_only=True)

	class Meta:
		model = Subcounty
		fields = (
			'id',
			'name',
			'county',
			'wards',
		)

class CountySerializer(serializers.ModelSerializer):
	subcounties = SubcountySerializer(many=True, read_only=True)

	class Meta:
		model = County
		fields = (
			'id',
			'name',
			'subcounties',
		)