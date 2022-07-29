from django.conf import settings
from django.core.files.images import get_image_dimensions
from rest_framework import serializers

from .models import Organization, AccountOrganization


class AccountOrganizationSerializer(serializers.ModelSerializer):
    account = serializers.SerializerMethodField()

    class Meta:
        model = AccountOrganization
        fields = ['title', 'account']

    def get_account(self, obj):
        request = self.context.get('request')
        if obj.account:
            file_url = obj.account.url
            # path = f"https//:{settings.DOMAIN}{image_url}"
            path = request.build_absolute_uri(file_url)
            try:
                data = {
                    'src': path,
                }
                return data
            except Exception:
                return None
        else:
            return None


class OrganizationDetailSerializer(serializers.ModelSerializer):
    accounts = AccountOrganizationSerializer(many=True)

    class Meta:
        model = AccountOrganization
        fields = ['title', 'content', 'link', 'lider_position', 'lider_name', 'reception_days', 'accounts']


class OrganizationListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Organization
        fields = ['slug', 'title', 'link', 'image']

    def get_image(self, obj):
        request = self.context.get('request')

        if obj.image:
            image_url = obj.image.url
            # path = f"https//:{settings.DOMAIN}{image_url}"
            path = request.build_absolute_uri(image_url)
            try:
                w, h = get_image_dimensions(obj.image.file)
                data = {
                    'src': path,
                    'width': w,
                    'height': h,
                }
                return data
            except Exception:
                return None
        else:
            return None
