# Generated by Django 2.2.1 on 2019-06-16 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20190616_2340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='edit',
            name='star',
        ),
        migrations.AddField(
            model_name='edit',
            name='star',
            field=models.ManyToManyField(to='api.User'),
        ),
    ]
