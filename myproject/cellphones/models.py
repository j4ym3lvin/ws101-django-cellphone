from django.db import models

class Cellphone(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    release_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.brand} {self.model}"