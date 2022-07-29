from django.urls import path

from .views import DataDetailSerializer, DataListAPIView


urlpatterns = [
    path('', DataListAPIView.as_view),
    path('<slug>', DataDetailSerializer.as_view),
]