from rest_framework import serializers

from .models import Data
from menu.models import Menu


class MenuSerializer(serializers.ModelSerializer):
    parent = serializers.SlugRelatedField(slug_field='slug', read_only=True)

    class Meta:
        model = Menu
        fields = ['parent', 'slug']


class DataListSerializer(serializers.ModelSerializer):
    menu = MenuSerializer(many=True, read_only=True)

    class Meta:
        model = Data
        fields = ['title', 'content', 'menu']


class DataDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['title', 'content']