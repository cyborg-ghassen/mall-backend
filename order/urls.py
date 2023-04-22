from rest_framework.routers import DefaultRouter

from .views import *

routes = DefaultRouter()
routes.register(r'order', OrderViewSet, basename='order')
routes.register(r'clothing', ClothingOrderViewSet, basename='clothing')
routes.register(r'restaurant', RestaurantOrderViewSet, basename='restaurant')
routes.register(r'electronics', ElectronicsOrderViewSet, basename='electronics')


urlpatterns = [
    *routes.urls
]

