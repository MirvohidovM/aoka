from django.db import models
from django.db.models.signals import pre_save
from django.utils.crypto import get_random_string

from baseapp.models import BaseModel
from config.utils import  unique_slug_generator
from config.validation import validate_file_extension


class Organization(BaseModel):
    title = models.CharField(max_length=256, blank=True, null=True, verbose_name="Sarlavha")
    content = models.TextField(verbose_name='Mazmuni')
    link = models.URLField(max_length=500, null=True, blank=True, verbose_name="Havola")
    image = models.FileField(upload_to="images/organization", blank=True, null=True,
                             verbose_name="Rasm", validators=[validate_file_extension])
    index = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "organization"
        verbose_name = "Tashkilot "
        verbose_name_plural = "Tashkilotlar"
        ordering = ['index']

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()
        return super(Organization, self).delete(*args, **kwargs)


class AccountOrganization(models.Model):
    organization = models.ForeignKey(Organization, related_name='accounts', on_delete=models.CASCADE)
    title = models.CharField(max_length=510, verbose_name='Hisobot nomlanishi')
    account = models.FileField(upload_to='files/organization', blank=True, null=True,
                               verbose_name='Hisobot fayli')


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        title = ''
        if instance.title_uz is not None and instance.title_uz != '':
            title = instance.title_uz
        elif instance.title_uzb is not None and instance.title_uzb != '':
            title = instance.title_uzb
        elif instance.title_ru is not None and instance.title_ru != '':
            title = instance.title_ru
        elif instance.title_en is not None and instance.title_en != '':
            title = instance.title_en
        else:
            title = get_random_string(8, '0123456789')
        instance.slug = unique_slug_generator(instance, title=title)


pre_save.connect(slug_generator, sender=Organization)
