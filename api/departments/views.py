# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from rest_framework import permissions

from departments.models import (
	Department, 
	Patient
)
from departments.serializers import (
	DepartmentSerializer, 
	PatientSerializer
)

class DepartmentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class DepartmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly, )

class PatientListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class PatientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly, )