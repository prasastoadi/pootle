# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-02 18:25
from __future__ import unicode_literals

from django.db import migrations


def set_directory_tp_path(apps, schema_editor):
    dirs = apps.get_model("pootle_app.Directory").objects.all()
    for directory in dirs:
        if not directory.parent:
            continue

        parts = directory.pootle_path.lstrip("/").split("/")
        if len(parts) > 2:
            directory.tp_path = '/'.join([""] + parts[2:])
            directory.save()


class Migration(migrations.Migration):

    dependencies = [
        ('pootle_app', '0013_directory_tp_path'),
    ]

    operations = [
        migrations.RunPython(set_directory_tp_path),
    ]