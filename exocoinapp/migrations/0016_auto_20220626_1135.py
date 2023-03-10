# Generated by Django 3.2.1 on 2022-06-26 11:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exocoinapp', '0015_alter_member_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fbot',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('dur', models.CharField(blank=True, max_length=2000, null=True)),
                ('rate', models.CharField(blank=True, max_length=2000, null=True)),
                ('user', models.CharField(blank=True, max_length=2000, null=True)),
                ('abt', models.CharField(blank=True, max_length=2000, null=True)),
                ('price', models.CharField(blank=True, max_length=2000, null=True)),
                ('tendency', models.CharField(blank=True, max_length=2000, null=True)),
                ('market', models.CharField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gbot',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('dur', models.CharField(blank=True, max_length=2000, null=True)),
                ('rate', models.CharField(blank=True, max_length=2000, null=True)),
                ('user', models.CharField(blank=True, max_length=2000, null=True)),
                ('abt', models.CharField(blank=True, max_length=2000, null=True)),
                ('price', models.CharField(blank=True, max_length=2000, null=True)),
                ('tendency', models.CharField(blank=True, max_length=2000, null=True)),
                ('market', models.CharField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mbot',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('dur', models.CharField(blank=True, max_length=2000, null=True)),
                ('rate', models.CharField(blank=True, max_length=2000, null=True)),
                ('user', models.CharField(blank=True, max_length=2000, null=True)),
                ('abt', models.CharField(blank=True, max_length=2000, null=True)),
                ('price', models.CharField(blank=True, max_length=2000, null=True)),
                ('tendency', models.CharField(blank=True, max_length=2000, null=True)),
                ('market', models.CharField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='ava',
            field=models.CharField(blank=True, default=0.0, max_length=1000),
        ),
        migrations.AddField(
            model_name='member',
            name='cap',
            field=models.CharField(blank=True, default=0.0, max_length=1000),
        ),
        migrations.AddField(
            model_name='member',
            name='cardb',
            field=models.CharField(blank=True, default='open', max_length=1000),
        ),
        migrations.AddField(
            model_name='member',
            name='tbal',
            field=models.IntegerField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 26, 11, 35, 33, 760496), null=True),
        ),
    ]
