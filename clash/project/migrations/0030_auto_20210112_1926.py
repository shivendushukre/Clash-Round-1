# Generated by Django 3.1 on 2021-01-12 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0029_auto_20201126_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='level',
            field=models.CharField(default='fe', max_length=15),
        ),
    ]