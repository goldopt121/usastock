# Generated by Django 3.2.1 on 2021-09-13 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exocoinapp', '0008_history_ref'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='email',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
