from django.contrib import admin
from wimp_base.models.owner_model import OwnerAdmin
from wimp_base.models.pet_model import PetProfileAdmin
from wimp_base.models import Pet, Owner, SiteSettings

# Register your models here.
admin.site.register(Pet, PetProfileAdmin)
admin.site.register(Owner, OwnerAdmin)


class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(SiteSettings, SiteSettingsAdmin)