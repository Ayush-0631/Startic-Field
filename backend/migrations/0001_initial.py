# Generated by Django 3.2.6 on 2022-08-03 13:39

import backend.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('public', models.BooleanField(default=True)),
                ('desc', models.TextField(max_length=1000)),
                ('code', models.CharField(default=backend.models.generate_code, editable=False, max_length=20)),
                ('link', models.CharField(max_length=300)),
                ('tags', models.CharField(max_length=500)),
                ('img', models.ImageField(upload_to='events/')),
                ('live_date', models.DateTimeField()),
                ('duration', models.IntegerField(default=60)),
                ('importance', models.CharField(choices=[('Very Important', 'Very Important'), ('Kind Of Important', 'Kind Of Important'), ('Not Much Important', 'Not Much Important')], default='Kind Of', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(default=10)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='Male', max_length=20)),
                ('is_contributor', models.BooleanField(default=False)),
                ('bio', models.TextField(max_length=500, null=True)),
                ('xp', models.IntegerField(default=0, null=True)),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('college', models.CharField(max_length=500, null=True)),
                ('year', models.IntegerField(default=2021, null=True)),
                ('interest', models.CharField(default='startic-field,', max_length=200, null=True)),
                ('social', models.CharField(max_length=300, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReversePitch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('public', models.BooleanField(default=True)),
                ('desc', models.TextField(max_length=1000, null=True)),
                ('tags', models.CharField(max_length=500, null=True)),
                ('img', models.ImageField(upload_to='programs/')),
                ('is_active', models.BooleanField(default=False)),
                ('live_date', models.DateField()),
                ('question1', models.TextField(max_length=500, null=True)),
                ('question2', models.TextField(max_length=500, null=True)),
                ('question3', models.TextField(max_length=500, null=True)),
                ('program_type', models.CharField(choices=[('Individual', 'Individual'), ('Team', 'Team'), ('Mix', 'Mix')], default='Team', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('link', models.CharField(max_length=200, null=True)),
                ('members', models.CharField(max_length=500, null=True)),
                ('social1', models.CharField(max_length=200, null=True)),
                ('social2', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('supporters', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='backend.profile')),
            ],
        ),
        migrations.CreateModel(
            name='TempUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('age', models.IntegerField(default=10)),
                ('college', models.CharField(max_length=500, null=True)),
                ('year', models.IntegerField(default=2021, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('answer1', models.TextField(max_length=1200, null=True)),
                ('answer2', models.TextField(max_length=2000, null=True)),
                ('answer3', models.TextField(max_length=3000, null=True)),
                ('idea_type', models.CharField(max_length=200, null=True)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='backend.reversepitch')),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserEventMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='backend.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='backend.profile')),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(to='backend.TempUser'),
        ),
        migrations.AddField(
            model_name='team',
            name='program',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.reversepitch'),
        ),
    ]
