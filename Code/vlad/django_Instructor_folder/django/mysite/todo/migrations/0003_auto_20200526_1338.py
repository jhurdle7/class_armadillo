# Generated by Django 3.0.6 on 2020-05-26 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200526_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
