# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from rest_framework import permissions

from locations.models import (
	County, 
	Subcounty,
	Ward, 
	Village, 
)
from locations.serializers import (
	CountySerializer,
	SubcountySerializer,
	WardSerializer,
	VillageSerializer,
)

class CountyListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CountySerializer
    queryset = County.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly, )


class CountyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CountySerializer
    queryset = County.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly, )

class SubcountyListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = SubcountySerializer
    queryset = Subcounty.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly, )

class SubcountyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubcountySerializer
    queryset = Subcounty.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly, )

class WardListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = WardSerializer
    queryset = Ward.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly, )

class WardRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WardSerializer
    queryset = Ward.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly, )

class VillageListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = VillageSerializer
    queryset = Village.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly, )

class VillageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VillageSerializer
    queryset = Village.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly, )