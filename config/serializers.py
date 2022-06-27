
from rest_framework import serializers
from menu.models import Menu


class GlobalMenuSerializer(serializers.ModelSerializer):
    parent = serializers.SlugRelatedField(slug_field='slug', read_only=True)

    class Meta:
        model = Menu
        fields = ['parent', 'slug']


class GlobalSearchSerializer(serializers.Serializer):
    slug = serializers.SerializerMethodField()
    menu = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()
    model = serializers.SerializerMethodField()

    class Meta:
        fields = ('slug', 'menu', 'title', 'content', 'model')

    def get_slug(self, obj):
        if hasattr(obj, 'slug'):
            return obj.slug
        else:
            return None

    def get_model(self, obj):
        return str(type(obj)).strip("'<>").split('.')[-1]


    def get_title(self, obj):
        if hasattr(obj, 'title'):
            return obj.title
        elif hasattr(obj, 'name'):
            return obj.name
        else:
            return None

    def get_content(self, obj):
        if hasattr(obj, 'content'):
            return obj.content
        else:
            return None

    def get_menu(self, obj):
        if hasattr(obj, 'menu'):
            return GlobalMenuSerializer(obj.menu).data
        else:
            return None
