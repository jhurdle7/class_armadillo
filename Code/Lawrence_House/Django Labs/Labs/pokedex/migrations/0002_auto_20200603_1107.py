# Generated by Django 3.0.6 on 2020-06-03 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='height',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='weight',
            field=models.IntegerField(),
        ),
    ]