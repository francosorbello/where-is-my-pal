from django import forms
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.formfields import SplitPhoneNumberField as PhoneNumberFieldForm
from django.contrib import admin

class Owner(models.Model):
    name = models.CharField(max_length=100)
    instagram = models.CharField(max_length=250)
    phone_number = PhoneNumberField()
    def __str__(self):
        return self.name

class OwnerAdminForm(forms.ModelForm):
    phone_number = PhoneNumberFieldForm()
    class Meta:
        model = Owner
        fields = "__all__"

class OwnerAdmin(admin.ModelAdmin):
    form = OwnerAdminForm
