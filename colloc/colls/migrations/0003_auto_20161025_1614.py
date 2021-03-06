# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 13:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('colls', '0002_corpus'),
    ]

    operations = [
        migrations.CreateModel(
            name='query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corp', models.FileField(default=None, upload_to='')),
                ('window', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1)),
                ('rang', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1)),
                ('word', models.CharField(max_length=50)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='user_set',
            name='user_req',
        ),
        migrations.AddField(
            model_name='corpus',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='corpus',
            name='corp',
            field=models.FileField(upload_to='/home/john/PycharmProjects/colloc/corpora'),
        ),
        migrations.DeleteModel(
            name='user_set',
        ),
    ]
