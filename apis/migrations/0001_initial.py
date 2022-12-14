# Generated by Django 3.2.6 on 2022-08-03 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(max_length=300, null=True)),
                ('client_secret', models.CharField(max_length=300, null=True)),
                ('access_token', models.CharField(max_length=300, null=True)),
                ('refresh_token', models.CharField(max_length=300, null=True)),
                ('token_uri', models.CharField(max_length=300, null=True)),
                ('expiry', models.DateTimeField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.profile')),
            ],
        ),
    ]
