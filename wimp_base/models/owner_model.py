from django import forms
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.formfields import SplitPhoneNumberField as PhoneNumberFieldForm
from django.contrib import admin

class Owner(models.Model):
    name = models.CharField(max_length=100, blank=False)
    instagram = models.CharField(max_length=250, blank=True)
    phone_number = PhoneNumberField(blank=False)
    def __str__(self):
        return self.name

class OwnerAdminForm(forms.ModelForm):
    phone_number = PhoneNumberFieldForm()
    class Meta:
        model = Owner
        fields = "__all__"

class OwnerAdmin(admin.ModelAdmin):
    form = OwnerAdminForm
