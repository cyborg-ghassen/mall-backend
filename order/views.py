from rest_framework import viewsets

from .models import Order, ClothingOrder, RestaurantOrder, ElectronicsOrder
from .serializers import OrderSerializer, ClothingOrderSerializer, RestaurantOrderSerializer, ElectronicsOrderSerializer


# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ClothingOrderViewSet(viewsets.ModelViewSet):
    queryset = ClothingOrder.objects.all()
    serializer_class = ClothingOrderSerializer


class RestaurantOrderViewSet(viewsets.ModelViewSet):
    queryset = RestaurantOrder.objects.all()
    serializer_class = RestaurantOrderSerializer


class ElectronicsOrderViewSet(viewsets.ModelViewSet):
    queryset = ElectronicsOrder.objects.all()
    serializer_class = ElectronicsOrderSerializer
