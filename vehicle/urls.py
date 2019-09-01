from django.urls import path
from .views import (ListAndCreateVehicle, DetailAndDeleteVehicle,
                    VehicleCreateView, VehicleDeleteView, VehicleListView)

app_name = "vehicle"
urlpatterns = [
    path('<pk>/delete/',VehicleDeleteView.as_view(),name="delete"),
    path('list/',VehicleListView.as_view(),name="list"),
    path('create/',VehicleCreateView.as_view(),name="create"),
    path('', ListAndCreateVehicle.as_view(), name="index"),
    path('<pk>', DetailAndDeleteVehicle.as_view(), name="detail")
]
