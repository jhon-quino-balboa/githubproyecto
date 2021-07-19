from rest_framework import serializers
from reservas_hotel.models import Hotel



class ReservasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hotel
        fields = ['id','estado','detalle_habitacion','dias_estadia','datos_facturacion','identificacion_cliente','moto_pago','metodo_pago']

     