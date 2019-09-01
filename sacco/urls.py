from django.urls import path
from .views import (ListAndCreateSacco, DetailAndDeleteSacco,
                    SaccoCreateView, SaccoDeleteView, SaccoListView)

app_name = "sacco"
urlpatterns = [
    path('<pk>/delete/',SaccoDeleteView.as_view(),name="delete"),
    path('list/',SaccoListView.as_view(),name="list"),
    path('create/',SaccoCreateView.as_view(),name="create"),
    path('', ListAndCreateSacco.as_view(), name="index"),
    path('<pk>', DetailAndDeleteSacco.as_view(), name="detail")
]
