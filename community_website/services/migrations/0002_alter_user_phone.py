# Generated by Django 4.0 on 2021-12-22 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=30, verbose_name='Phone Number'),
        ),
    ]
