import json

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save
from django.dispatch import receiver

from offer.models import Offer
from offer.serializers import OfferSerializer


@receiver(post_save, sender=Offer)
def my_handler(sender, instance: Offer, **kwargs, ):
    print("in signal")
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"tack_{instance.tack_id}",
        {
            'type': 'chat_message',
            'message': OfferSerializer(instance).data
        }
    )
