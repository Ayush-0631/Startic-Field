from django.db import models
from django.contrib.auth.models import User
import string
import random

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=10, null=False)
    gender = models.CharField(max_length=20, default='Male', choices=[
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Others', 'Others')
        ],
    )
    is_contributor = models.BooleanField(default=False)
    bio = models.TextField(max_length=500, null=True)
    xp = models.IntegerField(default=0, null=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    college = models.CharField(max_length=500, null=True)
    interest = models.CharField(max_length=200, null=True, default='startic-field,')
    social = models.CharField(max_length=300, null=True)


class Program(models.Model):
    title = models.CharField(max_length=100)
    public = models.BooleanField(default=True)
    desc = models.TextField(max_length=1000)
    tags = models.CharField(max_length=500)
    img = models.ImageField(upload_to='programs/')
    live_date = models.DateField()
    question1 = models.TextField(max_length=500, null=True)
    question2 = models.TextField(max_length=500, null=True)
    question3 = models.TextField(max_length=500, null=True)
    program_type = models.CharField(max_length=20, default='Team', choices=[
            ('Individual', 'Individual'),
            ('Team', 'Team'),
            ('Mix', 'Mix')
        ],
    )


class UserProgram(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    program = models.ForeignKey(Program, on_delete=models.DO_NOTHING)
    date = models.DateField(auto_now_add=True)
    answer1 = models.TextField(max_length=1200, null=True)
    answer2 = models.TextField(max_length=2000, null=True)
    answer3 = models.TextField(max_length=3000, null=True)


class Startup(models.Model):
    name = models.CharField(max_length=200, null=True)
    link = models.CharField(max_length=200, null=True)
    members = models.CharField(max_length=500, null=True)
    social1 = models.CharField(max_length=200, null=True)
    social2 = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    supporters = models.IntegerField(null=True, default=0)


def generate_code():
    length=15
    base = string.ascii_lowercase + string.ascii_uppercase + string.digits
    while True:
        code = ''.join(random.choices(base, k=length))
        break
    return code

class Event(models.Model):
    title = models.CharField(max_length=100)
    public = models.BooleanField(default=True)
    desc = models.TextField(max_length=1000)
    code = models.CharField(max_length=20, default=generate_code, editable=False)
    link = models.CharField(max_length=300)
    tags = models.CharField(max_length=500)
    img = models.ImageField(upload_to='events/')
    live_date = models.DateTimeField()
    duration = models.IntegerField(default=120)
    importance = models.CharField(max_length=20,default='Kind Of', choices=[
            ('Very Important', 'Very Important'),
            ('Kind Of Important', 'Kind Of Important'),
            ('Not Much Important', 'Not Much Important')
        ],
    )

class UserEventMap(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    date = models.DateField(auto_now_add=True)

    