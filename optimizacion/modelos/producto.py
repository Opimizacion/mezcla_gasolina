from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    abreviatura = models.CharField(max_length=10)
    tipo = models.BinaryField()

    class Meta:
        ordering = ['pk']