from django.shortcuts import get_object_or_404,render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SeatSerializer
from .models import Seat


class ListAndCreateSeat(ListCreateAPIView):
        queryset = Seat.objects.all()
        serializer_class=SeatSerializer


class DetailAndDeleteSeat(RetrieveUpdateDestroyAPIView):
    queryset = Seat.objects.all()
    serializer_class=SeatSerializer
class SeatCreateView(CreateView):
    model = Seat
    template_name = "seats\create.html"
    success_url = reverse_lazy('seat:index')


class SeatListView(ListView):
    model = Seat
    template_name = "seats\list.html"


class SeatDeleteView(DeleteView):
    model = Seat
    success_url = reverse_lazy('seat:index')
