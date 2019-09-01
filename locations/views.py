from django.shortcuts import get_object_or_404,render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LocationSerializer
from .models import Location


class ListAndCreateLocation(ListCreateAPIView):
        queryset = Location.objects.all()
        serializer_class=LocationSerializer


class DetailAndDeleteLocation(RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class=LocationSerializer


class LocationCreateView(CreateView):
    model = Location
    template_name = "locations\create.html"
    success_url = reverse_lazy('sacco:index')


class LocationListView(ListView):
    model = Location
    template_name = "locations\list.html"


class LocationDeleteView(DeleteView):
    model = Location
    success_url = reverse_lazy('sacco:index')
