# Generated by Django 3.2.6 on 2022-07-28 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_alter_event_duration'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Program',
            new_name='ReversePitch',
        ),
    ]