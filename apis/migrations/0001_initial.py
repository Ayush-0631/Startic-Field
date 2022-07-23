# Generated by Django 3.2.6 on 2022-07-23 08:50

import apis.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('public', models.BooleanField(default=True)),
                ('desc', models.TextField(max_length=1000)),
                ('code', models.CharField(default=apis.models.generate_code, editable=False, max_length=20)),
                ('link', models.CharField(max_length=300)),
                ('tags', models.CharField(max_length=500)),
                ('img', models.ImageField(upload_to='events/')),
                ('live_date', models.DateField()),
                ('importance', models.CharField(choices=[('Very Important', 'Very Important'), ('Kind Of Important', 'Kind Of Important'), ('Not Much Important', 'Not Much Important')], default='Kind Of', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserEventMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='apis.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='backend.profile')),
            ],
        ),
    ]
