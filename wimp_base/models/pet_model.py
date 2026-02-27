from django.db import models
from .owner_model import Owner

class Pet(models.Model):
    name = models.CharField("Pet Name", max_length=50)
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name