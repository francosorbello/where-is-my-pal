from django.http import HttpResponse

def pet_detail(request, pet_id):
    return HttpResponse("You're looking at pet %s." % pet_id)