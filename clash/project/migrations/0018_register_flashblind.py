# Generated by Django 3.1 on 2020-10-19 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0017_register_freezetimestart'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='flashblind',
            field=models.IntegerField(default=0),
        ),
    ]