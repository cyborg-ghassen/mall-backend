from rest_framework import viewsets

from .models import ElectronicsShop, ElectronicsItem
from .serializers import ElectronicsShopSerializer, ElectronicsItemSerializer


# Create your views here.
class ShopViewSet(viewsets.ModelViewSet):
    queryset = ElectronicsShop.objects.all()
    serializer_class = ElectronicsShopSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = ElectronicsItem.objects.all()
    serializer_class = ElectronicsItemSerializer
