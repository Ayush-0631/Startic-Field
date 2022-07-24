# Generated by Django 3.2.6 on 2022-07-24 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_auto_20220724_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendartoken',
            name='client_id',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='calendartoken',
            name='client_secret',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='calendartoken',
            name='token_uri',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='calendartoken',
            name='access_token',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='calendartoken',
            name='refresh_token',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='calendartoken',
            name='token_type',
            field=models.CharField(max_length=300, null=True),
        ),
    ]