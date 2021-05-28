from django.db import models

# Create your models here.
class Product(models.Model):
    productName = models.CharField(max_length=70)
    companyName = models.CharField(max_length=70)
    imageUrl = models.URLField()
    description = models.TextField(max_length=100)

    def __str__(self):
        return f"Product: {self.productName} {self.companyName}"