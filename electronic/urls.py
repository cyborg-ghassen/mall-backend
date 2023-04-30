from rest_framework.routers import DefaultRouter

from .views import *

routes = DefaultRouter()
routes.register(r'shop', ShopViewSet, basename='shop')
routes.register(r'category', CategoryViewSet, basename='category')
routes.register(r'item', ItemViewSet, basename='item')


urlpatterns = [
    *routes.urls
]

