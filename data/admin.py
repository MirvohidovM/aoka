from django.contrib import admin

from .models import Data


class DataAdmin(admin.ModelAdmin):
    exclude = ('title', 'content', 'created_by', 'updated_by', 'slug')


admin.site.register(Data, DataAdmin)
