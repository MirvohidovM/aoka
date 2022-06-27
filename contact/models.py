from django.db import models
from solo.models import SingletonModel


class Contact(SingletonModel):
    position = models.CharField(max_length=250, blank=True, null=True, verbose_name='Lavozimi')
    phone = models.TextField(verbose_name='Telefon')
    email = models.TextField(verbose_name='E-mail')
    address = models.CharField(max_length=255, verbose_name='Manzil')
    transport = models.TextField(verbose_name='Transport')
    reception_days = models.TextField(verbose_name='Qabul kunlari')

    class Meta:
        db_table = 'contact'
        verbose_name = "Bog'lanish"
        verbose_name_plural = "Bog'lanish"
