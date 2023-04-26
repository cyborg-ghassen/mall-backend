from django.db import models


# Create your models here.

GENDER_CHOICES = (
    ("male", "Homme"),
    ("female", "Femme"),
)


class Brand(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    logo = models.ImageField(upload_to='brands/logos/')

    def __str__(self):
        return self.name


class ClothingItem(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="clothing", null=True, blank=True)
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True, blank=True)

    @property
    def brand_name(self):
        return self.brand.name if self.brand else ""

    def __str__(self):
        return self.name
