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

    def get_queryset(self):
        query = super().get_queryset()
        if self.request.GET.get("category"):
            query = query.filter(category=self.request.GET.get("category"))

        return query


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
