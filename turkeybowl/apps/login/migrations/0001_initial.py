# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'players',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('pref_time', models.DateField()),
                ('pref_location', models.CharField(max_length=255)),
                ('players', models.ForeignKey(to='login.Player')),
            ],
            options={
                'db_table': 'teams',
            },
        ),
    ]
