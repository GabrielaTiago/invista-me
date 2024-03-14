from django.db import models

# Create your models here.

class   Investment(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name