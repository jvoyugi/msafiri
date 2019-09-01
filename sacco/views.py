from django.shortcuts import get_object_or_404,render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SaccoSerializer
from .models import Sacco


class ListAndCreateSacco(ListCreateAPIView):
        queryset = Sacco.objects.all()
        serializer_class=SaccoSerializer


class DetailAndDeleteSacco(RetrieveUpdateDestroyAPIView):
    queryset = Sacco.objects.all()
    serializer_class=SaccoSerializer

class SaccoCreateView(CreateView):
    model = Sacco
    template_name = "sacco\create.html"
    success_url = reverse_lazy('sacco:index')


class SaccoListView(ListView):
    model = Sacco
    template_name = "sacco\list.html"


class SaccoDeleteView(DeleteView):
    model = Sacco
    success_url = reverse_lazy('sacco:index')
