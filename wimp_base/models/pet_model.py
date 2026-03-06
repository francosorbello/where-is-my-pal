from django.db import models
from django import forms
from .owner_model import Owner
from django.contrib import admin
import base64
from django.core.files.base import ContentFile

class Pet(models.Model):
    name = models.CharField("Pet Name", max_length=50)
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="pets/",default='pets/default.jpg')
    hidden = models.BooleanField(default=False,help_text="When hidden, the pet wont appear on the index page")
    def __str__(self) -> str:
        return self.name
    
class PetProfileAdminForm(forms.ModelForm):
    # cropped image is hidden, as it only holds the data for the cropped photo
    cropped_image = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Pet
        fields = '__all__'

class PetProfileAdmin(admin.ModelAdmin):
    form = PetProfileAdminForm

    # when saving model, replace the uploaded picture with a cropped version
    def save_model(self, request, obj, form, change):
        cropped_data = form.cleaned_data.get('cropped_image')
        if cropped_data:
            format, imgstr = cropped_data.split(';base64,')
            ext = format.split('/')[-1] # image type (eg: jpg, png, etc)
            obj.photo = ContentFile(base64.b64decode(imgstr), name=f'pet_pic.{ext}')
        super().save_model(request, obj, form, change)