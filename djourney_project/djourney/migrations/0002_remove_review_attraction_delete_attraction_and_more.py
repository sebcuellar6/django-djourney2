# Generated by Django 5.0.7 on 2024-07-14 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djourney', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='attraction',
        ),
        migrations.DeleteModel(
            name='Attraction',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
