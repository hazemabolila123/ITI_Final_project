# Generated by Django 4.2.4 on 2023-08-23 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminModule', '0005_book_return_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book',
        ),
    ]