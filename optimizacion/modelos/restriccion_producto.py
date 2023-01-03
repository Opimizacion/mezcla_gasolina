from django.db import models
from optimizacion.modelos.producto_final import ProductoFinal

class RestriccionProducto(models.Model):
    nombre = models.CharField(max_length=100)
    valor = models.FloatField()
    producto = models.ForeignKey(ProductoFinal, related_name="restricciones", on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre+' '+str(self.valor)
