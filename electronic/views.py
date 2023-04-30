from rest_framework import viewsets

from .models import ElectronicsShop, ElectronicsItem, Category
from .serializers import ElectronicsShopSerializer, ElectronicsItemSerializer, CategorySerializer


# Create your views here.
class ShopViewSet(viewsets.ModelViewSet):
    queryset = ElectronicsShop.objects.all()
    serializer_class = ElectronicsShopSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = ElectronicsItem.objects.all()
    serializer_class = ElectronicsItemSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
