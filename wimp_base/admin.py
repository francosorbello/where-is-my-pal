from django.contrib import admin
from wimp_base.models.owner_model import OwnerAdmin
from wimp_base.models import Pet, Owner

# Register your models here.
admin.site.register(Pet)
admin.site.register(Owner, OwnerAdmin)