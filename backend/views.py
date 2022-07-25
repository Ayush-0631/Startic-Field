from django.shortcuts import render
from .models import *
from apis.views.calendar import *
from django.http import JsonResponse
# Create your views here.


def enroll_in_event(request, code):
    event = Event.objects.get(code=code)
    profile = Profile.objects.get(user=request.user)
    add_event_to_calendar(profile=profile, event=event)
    UserEventMap.objects.create(event=event, user=profile)

def Home(request):
    return render(request,"index.html")


def Signup(request):
    return render(request,"sign-up.html")


def Programs(request):
    return render(request,"Programs-page.html")


def Reverseptich(request):
    return render(request,"reverse-pitch.html")


def About(request):
    return render(request,"about-us.html")


def Contact(request):
    return render(request,"contact.html")
