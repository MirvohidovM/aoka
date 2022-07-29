from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from .models import Data
from .serializers import DataDetailSerializer, DataListSerializer


class DataDetailAPIView(RetrieveAPIView):
    authentication_classes = ()
    permission_classes = (AllowAny)
    queryset = Data.objects.all()
    serializer_class = DataDetailSerializer
    lookup_field = 'slug'


class DataListAPIView(ListAPIView):
    authentication_classes = ()
    permission_classes = (AllowAny)
    queryset = Data.objects.all()
    serializer_class = DataListSerializer
