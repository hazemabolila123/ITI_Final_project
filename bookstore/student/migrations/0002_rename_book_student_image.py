# Generated by Django 4.2.4 on 2023-08-21 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='book',
            new_name='image',
        ),
    ]
