from rest_framework import serializers

from tack.models import Tack


class TackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tack
        fields = "__all__"
