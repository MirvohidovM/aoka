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