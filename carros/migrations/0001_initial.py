# Generated by Django 3.1.1 on 2020-10-03 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=30)),
                ('fabricante', models.CharField(max_length=30)),
                ('cor', models.CharField(max_length=30)),
                ('ano', models.IntegerField()),
                ('Km', models.FloatField()),
            ],
        ),
    ]
