# Generated by Django 3.2.11 on 2023-10-19 16:28

from django.db import migrations

T = "tonic"
S = "subdominant"
D = "dominant"
A = "applied"

data = {
    "Freedom 2040 (Band) Melody": [T, T, S, T, T, S, D, T, T, S, D, T, S, S, D, T],
    "Freedom 2040 (Orchestra) Melody": [T, T, S, T, T, S, D, T, T, S, D, T, S, S, D, T],
    "Down by the Riverside Melody": [T, T, T, D, T, T, T, D, T, S, T, D, T],
    "Deep River Melody": [T, T, S, D, T, S, D, D, T, T, S, S],
    "I Want to be Ready Melody": [T, T, S, T, D, T, S, T],
    "The Favorite Melody": [D, T, T, D, D, T, T, D, D, A, T, A, T, S, D, T, D],
}


def update_site_forward(apps, schema_editor):
    Part = apps.get_model("musics", "Part")
    pattenered_parts = Part.objects.filter(name__in=list(data))
    for p in pattenered_parts:
        p.chord_scale_pattern = data[p.name]
        p.save()


class Migration(migrations.Migration):
    dependencies = [
        ("musics", "0022_part_chord_scale_pattern"),
    ]

    operations = [migrations.RunPython(update_site_forward, migrations.RunPython.noop)]
