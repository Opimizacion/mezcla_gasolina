from django.db import models

class ProductoFinal(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    demandaMin = models.FloatField()
    demandaMax = models.FloatField()

    class Meta:
        ordering = ['pk']
        
    def __str__(self):
        return self.nombre  