# Generated by Django 3.0.6 on 2020-05-28 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('age', models.IntegerField(default=0)),
                ('birthday', models.DateField()),
                ('phone_number', models.CharField(max_length=200)),
                ('is_cell', models.BooleanField()),
                ('comments', models.TextField(max_length=200)),
            ],
        ),
    ]
