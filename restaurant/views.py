from rest_framework import viewsets

import restaurant
from .models import Restaurant, MenuItem
from .serializers import RestaurantSerializer, MenuItemSerializer


# Create your views here.
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        query = super().get_queryset()
        if self.request.GET.get("restaurantID"):
            query = query.filter(restaurant=self.request.GET.get("restaurantID"))

        return query
