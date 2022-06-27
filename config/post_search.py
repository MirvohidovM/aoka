from itertools import chain
from rest_framework import generics
from rest_framework.permissions import AllowAny
from config.paginations import CustomPagination
from config.serializers import GlobalSearchSerializer
from equipments.models import Equipment
from event.models import Event
from faq.models import Faq
from gallery.models import PhotoGallery, VideoGallery
from internship.models import Intern
from opendata.models import Opendata
from post.models import Post
from vacancy.models import Vacancy
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
            intern = Intern.objects.filter(Q(name_uz__icontains=q)).filter(is_active=True)
            equipment = Equipment.objects.filter(Q(name_uz__icontains=q) | Q(content_uz__icontains=q)).filter(is_active=True)
            event = Event.objects.filter(Q(title_uz__icontains=q) | Q(content_uz__icontains=q) | Q(main_topic_uz__icontains=q)).filter(is_active=True)
            faq = Faq.objects.filter(Q(question_uz__icontains=q) | Q(answer_uz__icontains=q)).filter(is_active=True)
            opendata = Opendata.objects.filter(Q(title_uz__icontains=q) | Q(ilova_uz__icontains=q)).filter(is_active=True, menu__is_active=True)
            photo = PhotoGallery.objects.filter(Q(name_uz__icontains=q)).filter(is_active=True)
            video = VideoGallery.objects.filter(Q(name_uz__icontains=q)).filter(is_active=True)
            post = Post.objects.filter(Q(title_uz__icontains=q) | Q(content_uz__icontains=q)).filter(is_active=True, menu__is_active=True)
            vacancy = Vacancy.objects.filter(Q(title_uz__icontains=q) | Q(content_uz__icontains=q)).filter(is_active=True)
            
            return list(chain(event, equipment, faq, intern, opendata, photo, video, post, vacancy))
        elif lang == 'uzb':
            intern = Intern.objects.filter(Q(name_uzb__icontains=q)).filter(is_active=True)
            equipment = Equipment.objects.filter(Q(name_uzb__icontains=q) | Q(content_uzb__icontains=q)).filter(is_active=True)
            event = Event.objects.filter(Q(title_uzb__icontains=q) | Q(content_uzb__icontains=q) | Q(main_topic_uzb__icontains=q)).filter(is_active=True)
            faq = Faq.objects.filter(Q(question_uzb__icontains=q) | Q(answer_uzb__icontains=q)).filter(is_active=True)
            opendata = Opendata.objects.filter(Q(title_uzb__icontains=q) | Q(ilova_uzb__icontains=q)).filter(is_active=True, menu__is_active=True)
            photo = PhotoGallery.objects.filter(Q(name_uzb__icontains=q)).filter(is_active=True)
            video = VideoGallery.objects.filter(Q(name_uzb__icontains=q)).filter(is_active=True)
            post = Post.objects.filter(Q(title_uzb__icontains=q) | Q(content_uzb__icontains=q)).filter(is_active=True, menu__is_active=True)
            vacancy = Vacancy.objects.filter(Q(title_uzb__icontains=q) | Q(content_uzb__icontains=q)).filter(is_active=True)
            
            return list(chain(event, equipment, faq, intern, opendata, photo, video, post, vacancy))
        elif lang == 'ru':
            intern = Intern.objects.filter(Q(name_ru__icontains=q)).filter(is_active=True)
            equipment = Equipment.objects.filter(Q(name_ru__icontains=q) | Q(content_ru__icontains=q)).filter(is_active=True)
            event = Event.objects.filter(Q(title_ru__icontains=q) | Q(content_ru__icontains=q) | Q(main_topic_ru__icontains=q)).filter(is_active=True)
            faq = Faq.objects.filter(Q(question_ru__icontains=q) | Q(answer_ru__icontains=q)).filter(is_active=True)
            opendata = Opendata.objects.filter(Q(title_ru__icontains=q) | Q(ilova_ru__icontains=q)).filter(is_active=True, menu__is_active=True)
            photo = PhotoGallery.objects.filter(Q(name_ru__icontains=q)).filter(is_active=True)
            video = VideoGallery.objects.filter(Q(name_ru__icontains=q)).filter(is_active=True)
            post = Post.objects.filter(Q(title_ru__icontains=q) | Q(content_ru__icontains=q)).filter(is_active=True, menu__is_active=True)
            vacancy = Vacancy.objects.filter(Q(title_ru__icontains=q) | Q(content_ru__icontains=q)).filter(is_active=True)
            
            return list(chain(event, equipment, faq, intern, opendata, photo, video, post, vacancy))
        else:
            intern = Intern.objects.filter(Q(name_en__icontains=q)).filter(is_active=True)
            equipment = Equipment.objects.filter(Q(name_en__icontains=q) | Q(content_en__icontains=q)).filter(is_active=True)
            event = Event.objects.filter(Q(title_en__icontains=q) | Q(content_en__icontains=q) | Q(main_topic_en__icontains=q)).filter(is_active=True)
            faq = Faq.objects.filter(Q(question_en__icontains=q) | Q(answer_en__icontains=q)).filter(is_active=True)
            opendata = Opendata.objects.filter(Q(title_en__icontains=q) | Q(ilova_en__icontains=q)).filter(is_active=True, menu__is_active=True)
            photo = PhotoGallery.objects.filter(Q(name_en__icontains=q)).filter(is_active=True)
            video = VideoGallery.objects.filter(Q(name_en__icontains=q)).filter(is_active=True)
            post = Post.objects.filter(Q(title_en__icontains=q) | Q(content_en__icontains=q)).filter(is_active=True, menu__is_active=True)
            vacancy = Vacancy.objects.filter(Q(title_en__icontains=q) | Q(content_en__icontains=q)).filter(is_active=True)
            
            return list(chain(event, equipment, faq, intern, opendata, photo, video, post, vacancy))