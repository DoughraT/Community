# Generated by Django 4.0 on 2021-12-22 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_rename_provider_service_provider_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='provider_id',
            new_name='provider',
        ),
    ]
