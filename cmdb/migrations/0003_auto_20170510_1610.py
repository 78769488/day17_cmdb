# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 08:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0002_auto_20170510_1608'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'verbose_name': '应用', 'verbose_name_plural': '应用'},
        ),
        migrations.AlterModelOptions(
            name='business',
            options={'verbose_name': '业务线', 'verbose_name_plural': '业务线'},
        ),
        migrations.AlterModelOptions(
            name='host',
            options={'verbose_name': '主机信息', 'verbose_name_plural': '主机信息'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户信息', 'verbose_name_plural': '用户信息'},
        ),
    ]
