from rest_framework.routers import DefaultRouter

from .views import *

routes = DefaultRouter()
routes.register(r'shipment', ShipmentViewSet, basename='shipment')


urlpatterns = [
    *routes.urls
]

