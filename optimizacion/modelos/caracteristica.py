from django.db import models
from optimizacion.modelos.producto import Producto 

class Caracteristica(models.Model):
    nombre = models.CharField(max_length=100)
    valor = models.PositiveIntegerField()
    producto = models.ForeignKey(Producto, related_name="caracteristicas", on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre+' '+str(self.valor)