import uuid
from django.db import models

class QrPet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    redirect_to = models.CharField("Redirects to",max_length=255,blank=False)
    def __str__(self) -> str:
        return "Redirects to:"+self.redirect_to