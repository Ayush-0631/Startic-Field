from django.shortcuts import render
from .models import *
from apis.views.calendar import *
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import auth, messages
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
    live_pitch = ReversePitch.objects.get(is_active=True)
    form = UserProgram.objects.filter(user=request.user, program=live_pitch)
    if form.exists():
        return render(request, "programs-page.html", {'enrolled': True})
    return render(request, "programs-page.html", {'enrolled': False})


def Reverseptich(request):
    return render(request,"reverse-pitch.html")


def About(request):
    print(User.is_authenticated) 
    return render(request,"about-us.html")


def Contact(request):
    return render(request,"contact.html")


def Events(request):
    return render(request,"building.html")

def Signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.error(request, 'Password is too short')
                    return render(request, 'registeration.html')

                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.is_active = True
                user.save()
                return redirect('home')

            messages.warning(request, "This Email already exists!")
            return render(request, 'LoginPage.html')
        else:
            messages.warning(request, "This username already exists!")
            return render(request, 'LoginPage.html')

    return render(request,"LoginPage.html")

def login(request):
        username = request.POST['username']
        password = request.POST['password']
        if username and password:
            if User.objects.filter(username=username).exists():
                user = auth.authenticate(
                    username=username, password=password)
                if user:
                    if user.is_active:
                        auth.login(request, user)
                        messages.success(request,"loggedin succesfully")
                        return redirect("home")

                    messages.error(
                        request, "Account is not active,please check your email"
                    )

            elif User.objects.filter(email=username).exists():
                user = User.objects.get(email=username)
                user = auth.authenticate(
                    username=user.username, password=password)
                if user:
                    if user.is_active:
                        auth.login(request, user)
                        messages.success(request,"loggedin succesfully")
                        return redirect("home")

                    messages.error(
                        request, "Account is not active,please check your email"
                    )
            elif (User.objects.filter(email=username).exists() or User.objects.filter(username=username).exists() == False):
                messages.warning(
                    request, "The username or Email you have entered does not exist.")
                return render(request, 'login.html')

        messages.warning(request, 'Invalid credentials, try again')
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')


def FormsStudent(request):
    return render(request,"registerAsStudent.html")

def FormsStartup(request):
    return render(request,"registerYourStartUp.html")

def Formsreversepitch(request):
    return render(request,"reversePitchForm.html")

def FormsContributor(request):
    return render(request,"registerAsContributor.html")


def reverse_pitch(request):
    live_pitch = ReversePitch.objects.get(is_active=True)
    if request.method == 'GET':
        form = UserProgram.objects.filter(user=request.user, program=live_pitch)
        if form.exists():
            return render(request, 'reverse-pitch.html')
        return render(request, "reversePitchForm.html")
    
    profile = Profile.objects.create(
        user=request.user,
        age=request.POST.get('age'),
        gender=request.POST.get('gender'),
        college=request.POST.get('college'),
        year=request.POST.get('year'),
     )
    UserProgram.objects.create(
        user=request.user,
        program=live_pitch,
        answer1=request.POST.get('a1'),
        answer2=request.POST.get('a2'),
        answer3=request.POST.get('a3')
    )
    return redirect('home')

def Building(request):
    return render(request,"building.html")

def Registration(request):
    return render(request,"registration.html")