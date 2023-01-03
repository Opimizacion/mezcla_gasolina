from django.db import models

# Produccto intermedio
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    abreviatura = models.CharField(max_length=10)
    tipo = models.IntegerField(default=0)

    class Meta:
        ordering = ['pk']