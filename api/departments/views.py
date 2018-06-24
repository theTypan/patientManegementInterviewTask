# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from rest_framework import permissions

from departments.models import (
	Department, 
	DepartmentPatient
)
from departments.serializers import (
	DepartmentSerializer, 
	DepartmentPatientSerializer
)

class DepartmentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class DepartmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly, )

class DepartmentPatientListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = DepartmentPatientSerializer
    queryset = DepartmentPatient.objects.all()


class DepartmentPatientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DepartmentPatientSerializer
    queryset = DepartmentPatient.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly, )