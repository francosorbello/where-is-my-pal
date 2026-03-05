from django.contrib import admin
from wimp_base.models.owner_model import OwnerAdmin
from wimp_base.models.pet_model import PetProfileAdmin
from wimp_base.models import Pet, Owner

# Register your models here.
admin.site.register(Pet, PetProfileAdmin)
admin.site.register(Owner, OwnerAdmin)