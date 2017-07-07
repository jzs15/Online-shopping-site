# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-07 07:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255)),
                ('username', models.CharField(max_length=12, unique=True)),
                ('realname', models.CharField(default='', max_length=12)),
                ('phonenumber', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=255)),
                ('introduce', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_seller', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('total_score', models.FloatField(default=0)),
                ('total_customer', models.IntegerField(default=0)),
                ('avg_score', models.FloatField(default=0)),
                ('image', models.FileField(default='./images/default_image.jpg', upload_to='./images/', verbose_name='图片')),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=25)),
                ('money', models.DecimalField(decimal_places=2, default=0, max_digits=25)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='商品名')),
                ('content', models.TextField(verbose_name='商品说明')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='价格')),
                ('type', models.CharField(default='', max_length=10, verbose_name='种类')),
                ('image', models.FileField(default='./images/default_image.jpg', upload_to='./images/', verbose_name='图片')),
                ('total_score', models.FloatField(default=0)),
                ('total_customer', models.IntegerField(default=0)),
                ('avg_score', models.FloatField(default=0)),
                ('quantity', models.IntegerField(verbose_name='商品数量')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='', verbose_name='内容')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('score', models.FloatField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', related_query_name='reply', to='forum.Post')),
            ],
        ),
        migrations.CreateModel(
            name='UserItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
                ('product_author', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField(default=1, verbose_name='购买数量')),
                ('phonenumber', models.CharField(max_length=11, verbose_name='手机号')),
                ('address', models.CharField(max_length=255, verbose_name='地址')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('item_title', models.CharField(max_length=100)),
                ('image', models.FileField(default='./images/default_image.jpg', upload_to='')),
                ('is_purchased', models.BooleanField(default=False)),
                ('is_in_cart', models.BooleanField(default=False)),
                ('is_scored', models.BooleanField(default=False)),
                ('is_sended', models.BooleanField(default=False)),
                ('is_received', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
