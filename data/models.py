from django.db import models
from mptt.models import TreeForeignKey

from baseapp.models import BaseModel
from menu.models import Menu


class Data(BaseModel):
    title = models.CharField(max_length=512, verbose_name='Mavzu')
    content = models.TextField(verbose_name='Matni')
    menu = TreeForeignKey(Menu, null=True, blank=True, related_name='data',
                             on_delete=models.SET_NULL, verbose_name='Menyu')

    class Meta:
        db_table = 'data'
        verbose_name = "Ma'lumotnoma"
        verbose_name_plural = "Ma'lumotnomalar"

    def __str__(self):
        return self.title


class DataDownload(BaseModel):
    title = models.CharField(max_length=512, verbose_name='Mavzu')
    file = models.FileField(upload_to='files/DataDownload', verbose_name='Fayl')
    menu = TreeForeignKey(Menu, null=True, blank=True, related_name='data',
                             on_delete=models.SET_NULL, verbose_name='Menyu')

    class Meta:
        db_table = 'data_download'
        verbose_name = "Yuklanib olinuvchi ma'lumotnoma"
        verbose_name_plural = "Yuklanib olinuvchi ma'lumotnomalar"

    def __str__(self):
        return self.title