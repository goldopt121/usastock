# Generated by Django 3.2.1 on 2021-09-15 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exocoinapp', '0010_alter_history_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='addup',
            field=models.IntegerField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='msg',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
