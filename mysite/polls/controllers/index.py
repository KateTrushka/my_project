from django.http import HttpResponse
from django.shortcuts import redirect, render


def index(request):
    return render(request, 'main.html', {})

def about(request):
    return render(request, 'about.html', {})

def aboutWork(request):
    return HttpResponse("I'm a designer. I do presentations, posts and stories for Instagram, VK and Telegram, cards for WB, chek-lists, logotyps. Also I draw illustrations")

def aboutStudy(request):
    return HttpResponse("School of design by Elina Chebotareva")

def aboutExperience(request):
    return HttpResponse("Designer in a Musical studio, designer in the Instagram, designer in the online school EgeLand")
