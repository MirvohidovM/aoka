from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from organizations import serializers
from organizations.models import Organization


class OrganizationListView(ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = serializers.OrganizationListSerializer

    def get_queryset(self):
        queryset = Organization.objects.all().order_by('-created_at')[0:4]
        return queryset


class OrganizationDetailView(RetrieveAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = serializers.OrganizationDetailSerializer
    lookup_field = 'slug'