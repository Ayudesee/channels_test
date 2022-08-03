from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from group.models import Group
from group.serializers import GroupSerializer


class GroupViewset(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
