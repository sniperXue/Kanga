# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-16 08:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(default=b'', max_length=100, unique=True)),
                ('content', models.TextField(default=b'')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConnectedDevice',
            fields=[
                ('deviceType', models.CharField(choices=[(b'ARTIK5', b'Artik5'), (b'ARTIK7', b'Artik7'), (b'ARTIK10', b'Artik10'), (b'Raspberry Pi2', b'Raspberry Pi2'), (b'Raspberry Pi3', b'Raspberry Pi3'), (b'ODROID-XU4', b'Odroid-xu4'), (b'Linux-PC', b'Linux-pc'), (b'Windows-PC', b'Windows-pc')], max_length=50)),
                ('ip', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('hostname', models.CharField(default=b'', max_length=50, null=True)),
                ('description', models.TextField(default=b'', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DatabaseService',
            fields=[
                ('connection_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('db_name', models.CharField(max_length=150)),
                ('user', models.CharField(blank=True, default=b'', max_length=30)),
                ('password', models.CharField(blank=True, default=b'', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='JobScript',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'', max_length=50)),
                ('description', models.TextField(default=b'')),
                ('script', models.TextField(default=b'')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('ip', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('hostname', models.CharField(max_length=40)),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Cluster')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('port', models.IntegerField()),
                ('code', models.CharField(choices=[(b'KAFKA', b'Kafka'), (b'STORM', b'Storm'), (b'ELASTICSEARCH', b'ElasticSearch'), (b'ZOOKEEPER', b'Zookeeper'), (b'DJANGO', b'Django'), (b'POSTGRESQL', b'PostgreSql'), (b'SQLITE', b'Sqlite'), (b'OS', b'OperatingSystem')], max_length=15)),
                ('active', models.CharField(choices=[(b'BUSY', b'Busy'), (b'GOOD', b'Good'), (b'WARN', b'Warning'), (b'ERR', b'Error')], max_length=4)),
                ('purpose', models.CharField(choices=[(b'SERVICE', b'Service_port'), (b'MONITORING', b'Monitoring_port')], max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Node')),
            ],
        ),
        migrations.AddField(
            model_name='databaseservice',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Service'),
        ),
        migrations.AddField(
            model_name='config',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Service'),
        ),
    ]
