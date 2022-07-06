from django.contrib import admin

from .models import Lidership, CentralApparatus, RegionalAdministration


class LidershipAdmin(admin.ModelAdmin):
    ordering = ('index',)
    list_display = ['fullname_uz', 'fullname_uzb', 'fullname_ru', 'fullname_en',
                    'position_uz', 'position_uzb', 'position_ru', 'position_en',
                    'register_phone', 'index']
    # search_fields = ['fullname_ru', 'fullname_uz', 'fullname_uzb', 'fullname_en']
    # fields = ['position', 'fullname', 'biography', 'reception_times', 'register_phone', 'index']
    exclude = ['created_by', 'updated_by', 'is_active',
               'position', 'fullname', 'biography', 'reception_times']
    actions = ['delete_selected']

    def delete_selected(self, request, obj):
        for o in obj.all():
            o.delete()
    delete_selected.short_description = "O'chirish"

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super(LidershipAdmin, self).save_model(request, obj, form, change)


class CentralApparatusAdmin(admin.ModelAdmin):
    ordering = ('index',)
    list_display = ['fullname_uz', 'fullname_uzb', 'fullname_ru', 'fullname_en',
                    'position_uz', 'position_uzb', 'position_ru', 'position_en',
                    'phone', 'index']
    # search_fields = ['fullname_uz', 'fullname_uzb', 'fullname_ru', 'fullname_en',]
    # fields = ['position', 'fullname', 'responsibility', 'thumbnail', 'phone', 'email', 'index']
    exclude = ['created_by', 'updated_by', 'is_active',
               'position', 'fullname', 'responsibility']
    actions = ['delete_selected']

    def delete_selected(self, request, obj):
        for o in obj.all():
            o.delete()
    delete_selected.short_description = "O'chirish"

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)


class RegionalAdministrationAdmin(admin.ModelAdmin):
    ordering = ('index',)
    list_display = ['fullname_uz', 'fullname_uzb', 'fullname_ru', 'fullname_en',
                    'regional_name_uz', 'regional_name_uzb', 'regional_name_ru', 'regional_name_en',
                    'phone', 'email', 'index']
    # search_fields = ['fullname_ru', 'fullname_uz', 'fullname_uzb', 'fullname_en',
    #                  'regional_name_uz', 'regional_name_uzb', 'regional_name_ru', 'regional_name_en']
    # fields = ['position', 'fullname', 'address', 'reception_times',
    #           'regional_name', 'phone', 'email', 'index']
    exclude = ['created_by', 'updated_by', 'is_active',  'position',
               'fullname', 'address', 'reception_times', 'regional_name']
    actions = ['delete_selected']

    def delete_selected(self, request, obj):
        for o in obj.all():
            o.delete()
    delete_selected.short_description = "O'chirish"

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(Lidership, LidershipAdmin)
admin.site.register(CentralApparatus, CentralApparatusAdmin)
admin.site.register(RegionalAdministration, RegionalAdministrationAdmin)