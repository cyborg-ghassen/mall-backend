from rest_framework.routers import DefaultRouter

from .views import BrandViewSet, ClothingViewSet

routes = DefaultRouter()
routes.register(r'brand', BrandViewSet, basename='brand')
routes.register(r'clothing', ClothingViewSet, basename='clothing')


urlpatterns = [
    *routes.urls
]
