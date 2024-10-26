# Generated by Django 5.1.2 on 2024-10-22 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Name', models.CharField(max_length=20)),
                ('Accountno', models.IntegerField(primary_key='Accountno', serialize=False)),
                ('Amount', models.FloatField()),
                ('DoB', models.DateField()),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]
