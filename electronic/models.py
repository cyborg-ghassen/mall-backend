from django.db import models


# Create your models here.
class ElectronicsShop(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    logo = models.ImageField(upload_to='shops/logos/')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class ElectronicsItem(models.Model):
    name = models.CharField(max_length=100)
    shop = models.ForeignKey(ElectronicsShop, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to="shops/items/", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
