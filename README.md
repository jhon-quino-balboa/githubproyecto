# githubproyecto

para el proyecto de reservas de habitaciones de un hotel
se utilizo la libreria de rest_framework (generic.ListCreateAPIView) el cual genera 
vistas genéricas de Django que ayuda a desarrollar atajos para patrones de uso comun
gracias a estas librerias se logro implementar los metodos ['POST', 'GET'. 'PUT', 'DELETE']
optimizando la interaccion con la base de datos SqLite3 

urls ==> http://127.0.0.1:8000/api/hotel (interfaz donde se realiza la accion de POST Y GET)
	 http://127.0.0.1:8000/api/hotel/1 ==[1 es el id de reserva] ((interfaz donde se realiza la accion de DELETE Y PUT)) 

ejemplo de como se muestra un resultado al hacer put
{
    "id": 2,
    "estado": "pendiente",
    "detalle_habitacion": "matrimonial",
    "dias_estadia": "5 dias",
    "datos_facturacion": "25684",
    "identificacion_cliente": "885254 CB",
    "moto_pago": "8000",
    "metodo_pago": "targeta"
}
