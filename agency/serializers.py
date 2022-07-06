from rest_framework import serializers
from django.core.files.images import get_image_dimensions

from .models import *


class LidershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lidership
        fields = ['position', 'fullname', 'biography', 'reception_times', 'register_phone', 'index']


class CentralApparatusSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = CentralApparatus
        fields = ['position', 'fullname', 'responsibility', 'thumbnail', 'phone', 'email', 'index']

    def get_thumbnail(self, obj):
        request = self.context.get('request')
        if obj.photo:
            image_url = obj.photo.url
            path = request.build_absolute_uri(image_url)
            try:
                w, h = get_image_dimensions(obj.photo.file)
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


class RegionalAdministrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionalAdministration
        fields = ['position', 'fullname', 'address', 'reception_times',
                  'regional_name', 'phone', 'email', 'index']