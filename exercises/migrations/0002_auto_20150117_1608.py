# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movement',
            old_name='name',
            new_name='patientExerciseData',
        ),
        migrations.RemoveField(
            model_name='movement',
            name='orientation',
        ),
        migrations.RemoveField(
            model_name='movement',
            name='pose',
        ),
    ]
