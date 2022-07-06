from django.contrib import admin
from django.db import models
from django import forms
from tinymce.widgets import TinyMCE

from .models import News, NewsImages


class NewsImagesAdmin(admin.TabularInline):
    model = NewsImages
    extra = 1
    verbose_name = 'Yangilik Rasmi'
    verbose_name_plural = 'Yangilik Rasmlari'
    # formfield_overrides = {
    #     models.ImageField: {"widget": forms.ClearableFileInput(attrs={'multiple': True})},
    # }


class NewsForm(forms.ModelForm):
    content_uz = forms.CharField(label='Matn [uz]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    content_uzb = forms.CharField(label='Matn [uzb]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}),required=False)
    content_ru = forms.CharField(label='Matn [ru]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    content_en = forms.CharField(label='Matn [en]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    class Meta:
        model = News
        exclude = ['name', 'created_by', 'updated_by',
               'slug', 'views', 'title', 'content']


class NewsAdmin(admin.ModelAdmin):
    save_on_top = True
    ordering = ('-pub_date',)
    form = NewsForm

    list_filter = ['is_active', ]
    list_display = ['title_uz', 'pub_date', 'is_active', 'is_main']
    search_fields = ['title_ru', 'title_uz', 'title_uzb', 'title_en',
                     'content_uz', 'content_uzb', 'content_ru', 'content_en']
    exclude = ['name', 'created_by', 'updated_by',
               'slug', 'views', 'title', 'content']

    # filter_horizontal = ('',)
    inlines = [NewsImagesAdmin]
    actions = ['delete_selected']

    def delete_selected(self, request, obj):
        for o in obj.all():
            o.delete()

    delete_selected.short_description = "O'chirish"

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user

        obj.save()
        for filename, file in request.FILES.items():
            if filename == 'cover':
                continue
            pictures = request.FILES.getlist(filename)
            for picture in pictures[:-1]:
                NewsImages.objects.create(news=obj, image=picture)
        return super().save_model(request, obj, form, change)


admin.site.register(News, NewsAdmin)
