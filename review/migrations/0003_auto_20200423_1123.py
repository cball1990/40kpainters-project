# Generated by Django 3.0.5 on 2020-04-23 11:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('review', '0002_auto_20200419_1409'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='add_review',
            new_name='add_rev',
        ),
    ]
