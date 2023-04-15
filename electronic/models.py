from django.db import models


# Create your models here.
class ElectronicsShop(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    logo = models.ImageField(upload_to='shops/logos/')

    def __str__(self):
        return self.name


class ElectronicsItem(models.Model):
    name = models.CharField(max_length=100)
    shop = models.ForeignKey(ElectronicsShop, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
