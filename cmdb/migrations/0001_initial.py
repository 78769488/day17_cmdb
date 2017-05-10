# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 07:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='名称')),
                ('code', models.CharField(max_length=32, verbose_name='标识')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32, verbose_name='名称')),
                ('code', models.CharField(max_length=32, verbose_name='标识')),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(db_index=True, max_length=32, verbose_name='主机名称')),
                ('ip', models.GenericIPAddressField(db_index=True, verbose_name='IP')),
                ('port', models.IntegerField(verbose_name='Port')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.Business', verbose_name='业务线ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.Business', verbose_name='业务线ID')),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='app2host',
            field=models.ManyToManyField(to='cmdb.Host'),
        ),
    ]
