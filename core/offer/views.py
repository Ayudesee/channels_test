from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from offer.models import Offer
from offer.serializers import OfferSerializer


class OfferViewset(ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
