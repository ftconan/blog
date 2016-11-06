# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('classificationId', models.CharField(max_length=36, serialize=False, primary_key=True)),
                ('classificationIdlLevel', models.IntegerField()),
                ('parentDirectory', models.CharField(max_length=36, null=True, blank=True)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('classificationName', models.CharField(max_length=50)),
                ('classificationFormat', models.IntegerField()),
                ('classificationOrder', models.IntegerField()),
                ('isShow', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('commentId', models.CharField(max_length=36, serialize=False, primary_key=True)),
                ('commentary', models.TextField()),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('isShow', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('newsId', models.CharField(max_length=36, serialize=False, primary_key=True)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=50)),
                ('briefPic', models.CharField(max_length=80, null=True, blank=True)),
                ('briefNews', models.CharField(max_length=150, null=True, blank=True)),
                ('content', models.TextField()),
                ('status', models.IntegerField()),
                ('isTop', models.BooleanField(default=0)),
                ('alterTime', models.DateTimeField(auto_now_add=True)),
                ('browseVolume', models.IntegerField(default=0)),
                ('classificationId', models.ForeignKey(to='cms.Classification')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('pictureId', models.CharField(max_length=36, serialize=False, primary_key=True)),
                ('pictureName', models.CharField(max_length=20)),
                ('picturePath', models.CharField(max_length=50)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('isShow', models.BooleanField(default=1)),
                ('classificationId', models.ForeignKey(to='cms.Classification')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.CharField(max_length=36, serialize=False, primary_key=True)),
                ('userAccount', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('userName', models.CharField(max_length=10)),
                ('state', models.IntegerField()),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('isShow', models.BooleanField(default=1)),
                ('sculpture', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='userId',
            field=models.ForeignKey(to='cms.User'),
        ),
    ]
