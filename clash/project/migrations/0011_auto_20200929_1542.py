# Generated by Django 3.1 on 2020-09-29 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_register_bool'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='logouttime',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
