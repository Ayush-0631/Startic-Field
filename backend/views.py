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


def Events(request):
    return render(request,"events_page.html")

def Signup(request):
    return render(request,"LoginPage.html")

def FormsStudent(request):
    return render(request,"registerAsStudent.html")

def FormsStartup(request):
    return render(request,"registerYourStartUp.html")

def Formsreversepitch(request):
    return render(request,"reversePitchForm.html")

def ReversePitch(request):
    rpRegistration = 0
    if (rpRegistration == 0):
        a = "reversePitchForm.html"
    elif (rpRegistration == 1):
        a = "reverse-pitch.html"
    return render(request,a)

def Building(request):
    return render(request,"building.html")

def Registration(request):
    return render(request,"registration.html")