import json

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save
from django.dispatch import receiver

from group.models import GroupMembers
from group.serializers import GroupMembersSerializer
from tack.models import Tack
from tack.serializers import TackSerializer


@receiver(post_save, sender=GroupMembers)
def my_handler(sender, instance: GroupMembers, **kwargs, ):
    print("in signal")
    channel_layer = get_channel_layer()
    print(f"in signal: {channel_layer.__dict__ = }")

    async_to_sync(channel_layer.group_send)(
        f"user_{instance.user_id}",
        {
            'type': 'group.add',
            'message': GroupMembersSerializer(instance).data
        }
    )
