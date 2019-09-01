from django.shortcuts import get_object_or_404,render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import VehicleSerializer
from .models import Vehicle


class ListAndCreateVehicle(ListCreateAPIView):
        queryset = Vehicle.objects.all()
        serializer_class=VehicleSerializer


class DetailAndDeleteVehicle(RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class=VehicleSerializer
class VehicleCreateView(CreateView):
    model = Vehicle
    template_name = "vehicles\create.html"
    success_url = reverse_lazy('vehicle:index')


class VehicleListView(ListView):
    model = Vehicle
    template_name = "vehicles\list.html"


class VehicleDeleteView(DeleteView):
    model = Vehicle
    success_url = reverse_lazy('vehicle:index')
