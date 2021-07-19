from django.db import models
# Create your models here.



class Hotel(models.Model):
    
    estado = models.CharField(max_length=10, blank=True)
    detalle_habitacion = models.CharField(max_length=100, blank=True)
    dias_estadia = models.CharField(max_length=10, blank=True)
    datos_facturacion = models.CharField(max_length=100, blank=True)
    identificacion_cliente = models.CharField(max_length=100, blank=True)
    moto_pago = models.CharField(max_length=10, blank=True)
    metodo_pago = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.identificacion_cliente