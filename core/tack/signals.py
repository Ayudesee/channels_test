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
    print(f"in signal: {channel_layer.__dict__ = }")
    async_to_sync(channel_layer.group_send)(
        f"group_{instance.group.id}",
        {
            'type': 'tack.add',
            'message': TackSerializer(instance).data
        }
    )
