# Generated by Django 3.1 on 2020-10-25 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0024_auto_20201025_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='allow',
            field=models.BooleanField(default=False),
        ),
    ]
