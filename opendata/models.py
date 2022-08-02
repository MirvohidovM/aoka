from django.db import models
from django.db.models.signals import pre_save
from django.utils.crypto import get_random_string
from mptt.models import TreeForeignKey

from baseapp.models import BaseModel
from config.utils import unique_slug_generator
from menu.models import Menu


class Opendata(BaseModel):
    title = models.CharField(max_length=500, verbose_name="Sarlavha")
    index = models.IntegerField(null=True, blank=True)
    link = models.URLField(max_length=500, null=True, blank=True, verbose_name="Asosiy Havola")
    menu = TreeForeignKey(Menu, related_name='opendata', null=True, blank=True,
                             on_delete=models.SET_NULL, verbose_name='Menyu')
    xml_link = models.URLField(max_length=500, null=True, blank=True, verbose_name="XML havolasi")
    csv_link = models.URLField(max_length=500, null=True, blank=True, verbose_name="CSV havolasi")
    json_link = models.URLField(max_length=500, null=True, blank=True, verbose_name="JSON havolasi")
    xls_link = models.URLField(max_length=500, null=True, blank=True, verbose_name="XLS havolasi")
    rdf_link = models.URLField(max_length=500, null=True, blank=True, verbose_name="RDF havolasi")

    class Meta:
        db_table = "open_data"
        verbose_name = "Ochiq ma'lumot"
        verbose_name_plural = "Ochiq ma'lumotlar"
        ordering = ('index', )

    def __str__(self) -> str:
        return self.title


class OpendataAttachments(BaseModel):
    title = models.CharField(max_length=512, verbose_name="Mavzusi")

    class Meta:
        db_table = 'opendata_attachments'
        verbose_name = "Qo'shimcha ma'lumot"
        verbose_name_plural = "Qo'shimcha ma'lumotlar"

    def __str__(self):
        return self.title


class OpendataAttachmentsFiles(models.Model):
    opendata_attachments = models.ForeignKey(
        OpendataAttachments, on_delete=models.CASCADE, related_name='files', verbose_name='Fayllar')
    name = models.CharField(max_length=255, verbose_name="Nomi")
    file = models.FileField(upload_to='files/OpendataAttachments')

    class Meta:
        db_table = "opendata_attachments_files"
        verbose_name = "Ochiq ma'lumot fayllari"
        verbose_name_plural = "Ochiq ma'lumotlar fayllari"


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        title = ""
        if instance.title_uz is not None and instance.title_uz != '':
            title = instance.title_uz
        elif instance.title_ru is not None and instance.title_ru != '':
            title = instance.title_ru
        elif instance.title_uzb is not None and instance.title_uzb != '':
            title = instance.title_uzb
        elif instance.title_en is not None and instance.title_en != '':
            title = instance.title_en
        else:
            title = get_random_string(8, '0123456789')
        instance.slug = unique_slug_generator(instance, title=title)


pre_save.connect(slug_generator, sender=Opendata)
pre_save.connect(slug_generator, sender=OpendataAttachments)
