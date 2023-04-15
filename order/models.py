from django.contrib.auth.models import User
from django.db import models

from brand.models import ClothingItem
from electronic.models import ElectronicsItem
from restaurant.models import MenuItem


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(ClothingItem, through='ClothingOrder', related_name='orders')
    restaurant_items = models.ManyToManyField(MenuItem, through='RestaurantOrder', related_name='orders')
    electronics_items = models.ManyToManyField(ElectronicsItem, through='ElectronicsOrder', related_name='orders')
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Order {self.id}'


class ClothingOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(ClothingItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.order} - {self.item.name}'


class RestaurantOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.order} - {self.item.name}'


class ElectronicsOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(ElectronicsItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.order} - {self.item.name}'
