from django import forms
from django.contrib import admin
from opendata.models import Opendata, OpendataAttachments, OpendataAttachmentsFiles


class OpenDataForm(forms.ModelForm):
    class Meta:
        model = Opendata
        exclude = (
        'title',
        'slug',
        'created_by',
        "updated_by",
        )
        widgets={
            'menu': forms.Select(attrs={'class': 'bootstrap-select', 'data-width':"80%"})
            }


class OpendataAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'menu','link', 'index')
    list_filter = ('menu',  )
    search_fields = ('title_ru', 'title_uz', 'title_uzb', 'title_en', 'link')
    form = OpenDataForm
    exclude = (
        'title',
        'slug',
        'created_by',
        "updated_by",
    )

    accounts = ['delete_selected']

    def delete_selected(self, obj):
        for o in obj.all():
            o.delete()

    delete_selected.short_description = "O'chirish"

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()


admin.site.register(Opendata, OpendataAdmin)


class OpendataAttachmentsFilesAdmin(admin.TabularInline):
    model = OpendataAttachmentsFiles
    extra = 1
    exclude = ['name',]
    verbose_name = 'Fayl'
    verbose_name_plural = "Fayllar"


class OpendataAttachmentsForm(forms.ModelForm):
    class Meta:
        model = OpendataAttachments
        exclude = (
        'title',
        'slug',
        'created_by',
        "updated_by",
        )
        widgets={
            'menu': forms.Select(attrs={'class': 'bootstrap-select', 'data-width':"80%"})
            }


class OpendataAttachmentsAdmin(admin.ModelAdmin):
    list_display = ('title_uz',)
    search_fields = ('title_ru', 'title_uz', 'title_uzb', 'title_en')
    form = OpenDataForm
    exclude = (
        'title',
        'slug',
        'created_by',
        "updated_by",
    )

    accounts = ['delete_selected']
    inlines = [OpendataAttachmentsFilesAdmin]

    def delete_selected(self, obj):
        for o in obj.all():
            o.delete()

    delete_selected.short_description = "O'chirish"

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()


admin.site.register(OpendataAttachments, OpendataAttachmentsAdmin)
