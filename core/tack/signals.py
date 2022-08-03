import json

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save
from django.dispatch import receiver
from tack.models import Tack
from tack.serializers import TackSerializer


@receiver(post_save, sender=Tack)
def my_handler(sender, instance: Tack, **kwargs, ):
    print("in signal")
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "chat_2",
        {
            'type': 'chat.message',
            'message': TackSerializer(instance).data
        }
    )

    async_to_sync(channel_layer.group_send)(
        "user_2",
        {
            'type': 'tack.add',
            'message': TackSerializer(instance).data
        }
    )
    async_to_sync(channel_layer.group_send)(
        "user_3",
        {
            'type': 'tack.add',
            'message': TackSerializer(instance).data
        }
    )
