from django.http import HttpResponse, Http404
from django.shortcuts import render
from wimp_base.models.pet_model import Pet
from wimp_base.models.owner_model import Owner

def pet_detail(request, pet_id):
    pet = None
    try:
        pet = Pet.objects.get(pk=pet_id)
        owner = pet.owner

        context = {
            "pet_name" : pet.name,
            "owner_name" : owner.name,
            "owner_phone" : owner.phone_number
        }
    except Pet.DoesNotExist:
        raise Http404(f"No pet with id ${pet_id}")
    except Owner.DoesNotExist:
        if pet != None:
            raise Http404(f"${pet.name} desnt have an owner")
        else:
            raise Http404("Invalid pet and/or owner")
    
    return render(request,"wimp_base/pet_detail.html",context)