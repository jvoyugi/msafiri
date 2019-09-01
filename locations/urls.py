from django.urls import path
from .views import (ListAndCreateLocation, DetailAndDeleteLocation,
                    LocationCreateView, LocationDeleteView, LocationListView)

app_name = "location"
urlpatterns = [
    path('<pk>/delete/',LocationDeleteView.as_view(),name="delete"),
    path('list/',LocationListView.as_view(),name="list"),
    path('create/',LocationCreateView.as_view(),name="create"),
    path('', ListAndCreateLocation.as_view(), name="index"),
    path('<pk>', DetailAndDeleteLocation.as_view(), name="detail")
]
