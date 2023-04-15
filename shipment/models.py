from django.db import models

from brand.models import Brand
from electronic.models import ElectronicsShop
from order.models import Order
from restaurant.models import Restaurant


# Create your models here.
class Shipment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True, blank=True)
    electronics_shop = models.ForeignKey(ElectronicsShop, on_delete=models.CASCADE, null=True, blank=True)
    shipping_date = models.DateField(null=True, blank=True)
