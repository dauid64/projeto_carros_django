# Generated by Django 4.1.7 on 2023-03-10 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='CPF',
            field=models.CharField(blank=True, max_length=11),
        ),
        migrations.AlterField(
            model_name='person',
            name='data_nasc',
            field=models.DateField(blank=True),
        ),
    ]
