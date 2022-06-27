from itertools import chain
from rest_framework import generics
from rest_framework.permissions import AllowAny
from config.paginations import CustomPagination
from config.serializers import GlobalSearchSerializer
from opendata.models import Opendata
from news.models import News
from django.utils.translation import get_language
from django.db.models import Q


class SearchView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = GlobalSearchSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        request = self.request
        q = request.GET.get('q', '')
        lang = get_language()

        if lang == 'uz':
            opendata = Opendata.objects.filter(Q(title_uz__icontains=q) | Q(ilova_uz__icontains=q)).filter(is_active=True, menu__is_active=True)
            news = News.objects.filter(Q(title_uz__icontains=q) | Q(content_uz__icontains=q)).filter(is_active=True, menu__is_active=True)

            return list(chain( opendata, news,))
        elif lang == 'uzb':
            opendata = Opendata.objects.filter(Q(title_uzb__icontains=q) | Q(ilova_uzb__icontains=q)).filter(is_active=True, menu__is_active=True)
            news = News.objects.filter(Q(title_uzb__icontains=q) | Q(content_uzb__icontains=q)).filter(is_active=True, menu__is_active=True)

            return list(chain(opendata, news, ))
        elif lang == 'ru':
            opendata = Opendata.objects.filter(Q(title_ru__icontains=q) | Q(ilova_ru__icontains=q)).filter(is_active=True, menu__is_active=True)
            news = News.objects.filter(Q(title_ru__icontains=q) | Q(content_ru__icontains=q)).filter(is_active=True, menu__is_active=True)

            return list(chain(opendata, news, ))
        else:
            opendata = Opendata.objects.filter(Q(title_en__icontains=q) | Q(ilova_en__icontains=q)).filter(is_active=True, menu__is_active=True)
            news = News.objects.filter(Q(title_en__icontains=q) | Q(content_en__icontains=q)).filter(is_active=True, menu__is_active=True)

            return list(chain(opendata, news, ))