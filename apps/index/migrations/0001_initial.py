# Generated by Django 2.0 on 2019-12-27 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=50)),
                ('std_year', models.DateField(unique_for_year=4)),
                ('note', models.CharField(max_length=255)),
            ],
        ),
    ]
