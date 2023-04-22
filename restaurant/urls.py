from rest_framework.routers import DefaultRouter

from .views import *

routes = DefaultRouter()
routes.register(r'restaurant', RestaurantViewSet, basename='restaurant')
routes.register(r'item', MenuItemViewSet, basename='item')


urlpatterns = [
    *routes.urls
]

