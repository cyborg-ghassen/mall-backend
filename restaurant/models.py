from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    logo = models.ImageField(upload_to='restaurants/logos/')
    slug = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="restaurants/menus/", null=True, blank=True)

    def __str__(self):
        return self.name
