# Generated by Django 3.1 on 2020-09-03 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_auto_20200903_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='bool',
            field=models.BooleanField(default=True),
        ),
    ]
