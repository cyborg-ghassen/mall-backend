from rest_framework import serializers

from .models import ElectronicsShop, ElectronicsItem, Category


class ElectronicsShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectronicsShop
        fields = "__all__"


class ElectronicsItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectronicsItem
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
