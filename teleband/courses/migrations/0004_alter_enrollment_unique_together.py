# Generated by Django 3.2.11 on 2022-01-12 15:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("courses", "0003_auto_20220110_2052"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="enrollment",
            unique_together={("user", "course")},
        ),
    ]