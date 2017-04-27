# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 15:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gameservice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='player1',
            field=models.ForeignKey(db_column='player1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contest_player1', to='gameservice.Player'),
        ),
        migrations.AddField(
            model_name='contest',
            name='player2',
            field=models.ForeignKey(db_column='player2', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contest_player2', to='gameservice.Player'),
        ),
    ]