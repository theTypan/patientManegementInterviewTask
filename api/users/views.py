# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from rest_framework import permissions

from users.models import User
from users.serializers import UserSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user_list_create', request=request, format=format),
        'departments': reverse('department_list_create', request=request, format=format),
        'patients': reverse('patient_list_create', request=request, format=format),
        'counties': reverse('county_list_create', request=request, format=format),
        'subcounties': reverse('subcounty_list_create', request=request, format=format),
        'wards': reverse('ward_list_create', request=request, format=format),
        'villages': reverse('village_list_create', request=request, format=format),
    })

class UserListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly, )