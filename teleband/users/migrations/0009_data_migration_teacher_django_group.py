# Generated by Django 3.2.11 on 2022-01-29 03:31

from django.db import migrations


def add_demo_to_group(apps, schema_editor):
    User = apps.get_model("users", "User")
    demodave = User.objects.filter(username="demodave").first()

    if demodave is None:
        return

    Group = apps.get_model("auth", "Group")
    teacher_group = Group.objects.get(name="Teacher")

    demodave.groups.add(teacher_group)
    demodave.save()


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0008_user_external_id"),
    ]

    operations = [migrations.RunPython(add_demo_to_group, migrations.RunPython.noop)]
