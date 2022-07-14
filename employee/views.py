from rest_framework.generics import ListAPIView

from .serializers import LidershipSerializer, CentralApparatusSerializer, RegionalAdministrationSerializer
from .models import Lidership, CentralApparatus, RegionalAdministration


class LidershipListView(ListAPIView):
    queryset = Lidership.objects.all()
    serializer_class = LidershipSerializer


class CentralApparatusListView(ListAPIView):
    queryset = CentralApparatus.objects.all()
    serializer_class = CentralApparatusSerializer


class RegionalAdministrationListView(ListAPIView):
    queryset = RegionalAdministration.objects.all()
    serializer_class = RegionalAdministrationSerializer