# Generated by Django 2.0.2 on 2018-02-12 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(
                default='my location default', max_length=120),
        ),
    ]