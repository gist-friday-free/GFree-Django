# Generated by Django 2.2.1 on 2019-05-11 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190511_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='grade',
            field=models.IntegerField(choices=[('Zero', 0), ('One', 1), ('Two', 2), ('Three', 3), ('Four', 4)]),
        ),
        migrations.AlterField(
            model_name='class',
            name='semester',
            field=models.IntegerField(choices=[('First', 1), ('Second', 2)]),
        ),
        migrations.AlterField(
            model_name='class',
            name='week1',
            field=models.CharField(blank=True, choices=[('Monday', 'mon'), ('Tuesday', 'tue'), ('Wednesday', 'wed'), ('Thursday', 'thu'), ('Friday', 'fri'), ('Saturday', 'sat'), ('Sunday', 'sun')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='class',
            name='week2',
            field=models.CharField(blank=True, choices=[('Monday', 'mon'), ('Tuesday', 'tue'), ('Wednesday', 'wed'), ('Thursday', 'thu'), ('Friday', 'fri'), ('Saturday', 'sat'), ('Sunday', 'sun')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='class',
            name='week3',
            field=models.CharField(blank=True, choices=[('Monday', 'mon'), ('Tuesday', 'tue'), ('Wednesday', 'wed'), ('Thursday', 'thu'), ('Friday', 'fri'), ('Saturday', 'sat'), ('Sunday', 'sun')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='class',
            name='week4',
            field=models.CharField(blank=True, choices=[('Monday', 'mon'), ('Tuesday', 'tue'), ('Wednesday', 'wed'), ('Thursday', 'thu'), ('Friday', 'fri'), ('Saturday', 'sat'), ('Sunday', 'sun')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='class',
            name='week5',
            field=models.CharField(blank=True, choices=[('Monday', 'mon'), ('Tuesday', 'tue'), ('Wednesday', 'wed'), ('Thursday', 'thu'), ('Friday', 'fri'), ('Saturday', 'sat'), ('Sunday', 'sun')], max_length=20, null=True),
        ),
    ]