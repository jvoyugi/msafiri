# Generated by Django 2.2.1 on 2019-06-23 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sacco', '0002_auto_20190623_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sacco',
            name='manager',
            field=models.CharField(max_length=100, verbose_name='Store manager'),
        ),
    ]
