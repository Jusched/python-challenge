# Generated by Django 4.1.4 on 2022-12-17 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('origin', models.CharField(max_length=15)),
                ('destination', models.CharField(max_length=15)),
                ('departure_date', models.DateField()),
                ('time_departure', models.TimeField()),
                ('duration', models.TimeField()),
            ],
        ),
    ]