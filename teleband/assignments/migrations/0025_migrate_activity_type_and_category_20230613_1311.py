# Generated by Django 3.2.11 on 2023-06-13 17:11

from django.db import migrations

def move_type_and_category(apps, schema_editor):
    Activity = apps.get_model("assignments", "Activity")
    ActivityType = apps.get_model("assignments", "ActivityType")
    ActivityCategory = apps.get_model("assignments", "ActivityCategory")
    for activity in Activity.objects.all():
        activity.activity_type_name = activity.activity_type.name
        activity.category = activity.activity_type.category.name
        activity.save()

class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0024_add_activity_type_and_category_fields'),
    ]

    operations = [
        migrations.RunPython(move_type_and_category)
    ]