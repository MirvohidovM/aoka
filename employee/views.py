from rest_framework.generics import ListAPIView, RetrieveAPIView

from .serializers import (LidershipSerializer,
                          CentralApparatusSerializer,
                          RegionalAdministrationSerializer,
                          PressSecretarySerializer,)
from .models import (Lidership,
                     CentralApparatus,
                     RegionalAdministration,
                     PressSecretary,)


class LidershipListView(ListAPIView):
    authentication_classes = ()
    queryset = Lidership.objects.all()
    serializer_class = LidershipSerializer


class CentralApparatusListView(ListAPIView):
    authentication_classes = ()
    queryset = CentralApparatus.objects.all()
    serializer_class = CentralApparatusSerializer


class RegionalAdministrationListView(ListAPIView):
    authentication_classes = ()
    queryset = RegionalAdministration.objects.all()
    serializer_class = RegionalAdministrationSerializer


class PressSecretaryAPIView(RetrieveAPIView):
    authentication_classes = ()
    queryset = PressSecretary.objects.all()
    serializer_class = PressSecretarySerializer
    lookup_field = 'pk'