from django.urls import path
from .views import (ListAndCreateSeat, DetailAndDeleteSeat,
                    SeatCreateView, SeatDeleteView, SeatListView)

app_name = "seat"
urlpatterns = [
    path('<pk>/delete/',SeatDeleteView.as_view(),name="delete"),
    path('list/',SeatListView.as_view(),name="list"),
    path('create/',SeatCreateView.as_view(),name="create"),
    path('', ListAndCreateSeat.as_view(), name="index"),
    path('<pk>', DetailAndDeleteSeat.as_view(), name="detail")
]
