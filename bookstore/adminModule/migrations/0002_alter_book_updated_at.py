# Generated by Django 4.2.4 on 2023-08-20 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminModule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
