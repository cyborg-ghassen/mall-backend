from rest_framework import serializers

from .models import Order, ClothingOrder, RestaurantOrder, ElectronicsOrder


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class ClothingOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingOrder
        fields = "__all__"


class RestaurantOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantOrder
        fields = "__all__"


class ElectronicsOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectronicsOrder
        fields = "__all__"
