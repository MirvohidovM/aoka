from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import Contact


class ContactAdmin(SingletonModelAdmin):
    exclude = ['address', 'transport', 'position', 'reseption_days',]

    actions = ['delete_selected']

    def delete_selected(self, request, obj):
        for o in obj:
            o.delete()

    delete_selected.short_description = "O'chirish"


admin.site.register(Contact, ContactAdmin)
