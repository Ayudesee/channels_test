from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from tack.models import Tack
from tack.serializers import TackSerializer


class TackViewset(ModelViewSet):
    queryset = Tack.objects.all()
    serializer_class = TackSerializer
