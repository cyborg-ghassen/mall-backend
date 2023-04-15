from rest_framework import viewsets

from .models import Brand, ClothingItem
from .serializers import BrandSerializer, ClothingItemSerializer


# Create your views here.
class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ClothingViewSet(viewsets.ModelViewSet):
    queryset = ClothingItem.objects.all()
    serializer_class = ClothingItemSerializer
