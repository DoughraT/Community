# Generated by Django 4.0 on 2021-12-22 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_alter_service_provider'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='provider',
            new_name='provider_id',
        ),
    ]
