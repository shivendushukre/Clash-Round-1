# Generated by Django 3.1 on 2021-01-16 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0035_auto_20210116_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='freezesec',
            field=models.IntegerField(default=0),
        ),
    ]
