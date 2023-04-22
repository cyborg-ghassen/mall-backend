from rest_framework import viewsets

from .models import Shipment
from .serializers import ShipmentSerializer


# Create your views here.
class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
