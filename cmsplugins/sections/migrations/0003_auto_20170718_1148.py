# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-18 09:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0002_wrap_cms_page'),
    ]

    operations = [
        migrations.RenameModel('Wrap', 'Section'),
        migrations.AlterField(
            model_name='section',
            name='cmsplugin_ptr',
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                related_name='sections_section',
                serialize=False,
                to='cms.CMSPlugin'
            ),
        ),
        migrations.RunSQL(
            [
                (
                    "UPDATE cms_cmsplugin"
                    " SET plugin_type = 'SectionPlugin'"
                    " WHERE plugin_type = 'WrapPlugin'"
                )
            ]
        ),
    ]