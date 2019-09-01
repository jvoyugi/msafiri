# Generated by Django 2.2.1 on 2019-06-18 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id',
                 models.AutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
                ('seat_number',
                 models.PositiveIntegerField()),
                ('is_taken',
                 models.BooleanField(
                     default=False)),
                ('vehicle',
                 models.ForeignKey(
                     on_delete=django.db.models.deletion.CASCADE,
                     to='vehicle.Vehicle')),
            ],
        ),
    ]
