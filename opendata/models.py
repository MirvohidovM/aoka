from menu.models import Menu
from django.db import models
from django.db.models.signals import pre_save
from django.utils.crypto import get_random_string
from mptt.models import TreeForeignKey
from baseapp.models import BaseModel
from config.utils import unique_slug_generator


def xml_directory(instance, filename):
    return 'opendata/xml/{}/{}'.format(instance.opendata.slug, filename)


def csv_directory(instance, filename):
    return 'opendata/csv/{}/{}'.format(instance.opendata.slug, filename)


def json_directory(instance, filename):
    return 'opendata/json/{}/{}'.format(instance.opendata.slug, filename)


def xls_directory(instance, filename):
    return 'opendata/xls/{}/{}'.format(instance.opendata.slug, filename)


def rdf_directory(instance, filename):
    return 'opendata/rdf/{}/{}'.format(instance.opendata.slug, filename)



class Opendata(BaseModel):
    title = models.CharField(max_length=500, verbose_name="Sarlavha")
    index = models.IntegerField(null=True, blank=True)
    # ilova = models.CharField(max_length=500, null=True, blank=True, verbose_name="Ilova")
    link = models.URLField(max_length=500, null=True, blank=True, verbose_name="Havola")
    menu = TreeForeignKey(Menu, related_name='opendata', null=True, blank=True,
                             on_delete=models.SET_NULL, verbose_name='Menyu')

    class Meta:
        db_table = "open_data"
        verbose_name = "Ochiq ma'lumot"
        verbose_name_plural = "Ochiq ma'lumotlar"
        ordering = ('index', )

    def __str__(self) -> str:
        return self.title


class OpendataAttachments(models.Model):
    opendata = models.ForeignKey(
        Opendata, on_delete=models.CASCADE, related_name='attachments', verbose_name='Fayllar')
    name = models.CharField(max_length=255, verbose_name="Nomi")
    xml = models.FileField(upload_to=xml_directory)
    csv = models.FileField(upload_to=csv_directory)
    json = models.FileField(upload_to=json_directory)
    xls = models.FileField(upload_to=xls_directory)
    rdf = models.FileField(upload_to=rdf_directory)

    class Meta:
        db_table = "open_data_attachments"
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
