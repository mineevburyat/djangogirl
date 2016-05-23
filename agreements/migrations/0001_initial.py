# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contractnumber', models.CharField(max_length=10)),
                ('startdata', models.DateTimeField(default=django.utils.timezone.now)),
                ('subject', models.TextField()),
                ('completdata', models.DateTimeField()),
                ('department', models.CharField(max_length=20)),
                ('profitable', models.BooleanField(default=False)),
                ('autoprolongation', models.BooleanField(default=False)),
            ],
        ),
    ]
