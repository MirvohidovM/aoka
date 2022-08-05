from django.db import models
from solo.models import SingletonModel

from baseapp.models import BaseModel


class Lidership(BaseModel):
    slug = None
    position = models.CharField(max_length=255, verbose_name='Lavozimi')
    fullname = models.CharField(max_length=255, verbose_name="To'liq ismi")
    biography = models.TextField(verbose_name='Biografiyasi')
    register_phone = models.CharField(max_length=30, verbose_name='Qabul raqami')
    reception_times = models.CharField(max_length=255, verbose_name='Qabul vaqtlari')
    index = models.PositiveSmallIntegerField(verbose_name='Tartib raqami')

    class Meta:
        db_table = 'lidership'
        verbose_name = 'Rahbar'
        verbose_name_plural = 'Rahbariyat'
        ordering = ('index',)

    def __str__(self):
        return f"{self.fullname} ({self.position})"


class CentralApparatus(BaseModel):
    slug = None
    position = models.CharField(max_length=255, verbose_name='Lavozimi')
    fullname = models.CharField(max_length=255, verbose_name="To'liq ismi")
    responsibility = models.TextField(verbose_name='Majburiyati')
    photo = models.ImageField(upload_to='CentralApparatus/photos/', verbose_name='Rasmi')
    phone = models.CharField(max_length=30, verbose_name='Qabul raqami')
    email = models.EmailField()
    index = models.PositiveSmallIntegerField(verbose_name='Tartib raqami')

    class Meta:
        db_table = 'central_apparatus'
        verbose_name = 'Markaziy apparat'
        verbose_name_plural = 'Markaziy apparat'
        ordering = ('index',)

    def __str__(self):
        return f"{self.fullname} ({self.position})"


class RegionalAdministration(BaseModel):
    slug = None
    position = models.CharField(max_length=255, verbose_name='Lavozimi')
    fullname = models.CharField(max_length=255, verbose_name="To'liq ismi")
    address = models.CharField(max_length=510, verbose_name="Manzil")
    phone = models.CharField(max_length=30, verbose_name='Qabul raqami')
    email = models.EmailField(verbose_name='Elektron pochta')
    reception_times = models.CharField(max_length=255, verbose_name='Qabul vaqtlari')
    regional_name = models.CharField(max_length=510, verbose_name='Hududiy nomi')
    index = models.PositiveSmallIntegerField(verbose_name='Tartib raqami')

    class Meta:
        db_table = 'regional_administration'
        verbose_name = 'Hududiy administratsiya'
        verbose_name_plural = 'Hududiy administratsiya'
        ordering = ('index',)

    def __str__(self):
        return self.regional_name


class PressSecretary(SingletonModel):
    fullname = models.CharField(max_length=255, verbose_name="To'liq ismi")
    biography = models.TextField(verbose_name='Biografiyasi')
    phone = models.CharField(max_length=30, verbose_name='Telefon raqami')
    email = models.EmailField()

    class Meta:
        db_table = 'press_secretary'
        verbose_name = 'Matbuot kotibi'
        verbose_name_plural = 'Matbuot kotibi'

    def __str__(self):
        return self.fullname