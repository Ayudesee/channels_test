import re

from rest_framework import serializers

from tack.models import Tack


class TackSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(max_digits=8, decimal_places=2, min_value=50)

    def to_representation(self, instance):
        data = super(TackSerializer, self).to_representation(instance)
        data["price"] = f"{float(data['price']) / 100:.2f}"

        return data

    def to_internal_value(self, data):
        price = data['price']
        if isinstance(price, str):
            if re.fullmatch(r"\.\d+", price):
                price = "0" + price
            if re.fullmatch(r"\d+\.\d{0,2}", price):
                price = int(round(float(price), 2) * 100)
        elif isinstance(price, float):
            price = int(round(price, 2) * 100)
        elif isinstance(price, int):
            price = price * 100
        data['price'] = price
        return super().to_internal_value(data)

    class Meta:
        model = Tack
        fields = "__all__"
