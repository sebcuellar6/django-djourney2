# Generated by Django 5.0.7 on 2024-07-14 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djourney', '0003_attraction_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='name',
            field=models.CharField(default='Unknown Attraction', max_length=35),
        ),
        migrations.AddField(
            model_name='city',
            name='name',
            field=models.CharField(default='Unknown City', max_length=35),
        ),
    ]