from django.shortcuts import render
from rest_framework import generics
from reservas_hotel.models import Hotel
from reservas_hotel.serializers import ReservasSerializer



class ReservasList(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = ReservasSerializer


class ReservasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel
    serializer_class = ReservasSerializer