# Generated by Django 4.1.5 on 2023-01-16 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0005_remove_entries_owner_entries_bathrooms_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entries',
            old_name='Furnisng',
            new_name='Furnishing',
        ),
    ]
