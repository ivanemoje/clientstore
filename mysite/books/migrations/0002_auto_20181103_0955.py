# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-11-03 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='account_manager',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='pages',
            new_name='capacity',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='publication_date',
            new_name='installation_date',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='price',
            new_name='monthly_charge',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='book',
            name='book_type',
        ),
        migrations.AddField(
            model_name='book',
            name='service_type',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Leased Line'), (2, 'IBW'), (3, 'Fixed Line')], null=True),
        ),
    ]
