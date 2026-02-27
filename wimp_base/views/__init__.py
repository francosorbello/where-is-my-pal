from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from wimp_base.models.pet_model import Pet
from .pet_views import *

def index(request):
    pets = Pet.objects.all()
    template = loader.get_template("index.html")
    context = {"pets" : pets}
    return render(request,"index.html",context)