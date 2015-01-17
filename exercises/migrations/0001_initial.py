# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('pose', models.CharField(max_length=250)),
                ('orientation', models.CommaSeparatedIntegerField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
