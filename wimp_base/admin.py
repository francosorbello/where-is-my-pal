from django.contrib import admin
from django.utils.html import format_html
from wimp_base.models.owner_model import OwnerAdmin
from wimp_base.models.pet_model import PetProfileAdmin
from wimp_base.models import Pet, Owner, SiteSettings, QrPet


admin.site.register(Pet, PetProfileAdmin)
admin.site.register(Owner, OwnerAdmin)


class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(SiteSettings, SiteSettingsAdmin)


@admin.register(QrPet)
class QrPetAdmin(admin.ModelAdmin):
    list_display = ('id', 'pet', 'redirect_to', 'qr_thumbnail')
    list_filter = ('pet',)
    search_fields = ('pet__name', 'redirect_to')
    readonly_fields = ('id', 'redirect_to', 'qr_image_preview', 'qr_image')
    ordering = ('-pk',)

    fieldsets = (
        (None, {
            'fields': ('pet',)
        }),
        ('QR Code', {
            'fields': ('redirect_to', 'qr_image_preview', 'qr_image')
        }),
    )

    def qr_thumbnail(self, obj):
        if obj.qr_image:
            return format_html('<img src="{}" width="50" height="50" />', obj.qr_image.url)
        return '-'
    qr_thumbnail.short_description = 'QR'

    def qr_image_preview(self, obj):
        if obj.qr_image:
            return format_html('<img src="{}" width="150" height="150" />', obj.qr_image.url)
        return '-'
    qr_image_preview.short_description = 'QR Code Preview'

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if obj.qr_image:
            obj.generate_qr_code()
            obj.save()
