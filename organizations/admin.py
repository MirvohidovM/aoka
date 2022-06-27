from django.contrib import admin

from organizations.models import Organization, AccountOrganization


class AccountOrganizationAdmin(admin.TabularInline):
    model = AccountOrganization
    extra = 1
    exclude = ['title',]
    verbose_name = 'Tashkilot hisoboti'
    verbose_name_plural = 'Tashkilot hisobotlari'


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ["title_uz", 'title_uzb', 'title_ru', 'title_en', 'link']

    exclude = (
        'title',
        'content',
        'slug',
        'created_by',
        'updated_by'
    )
    inlines = [AccountOrganizationAdmin]
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


admin.site.register(Organization, OrganizationAdmin)
