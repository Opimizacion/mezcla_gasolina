from django.db import models
from optimizacion.modelos.producto import Producto 

class Caracteristica(models.Model):
    nombre = models.CharField(max_length=100)
    valor = models.PositiveIntegerField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)