# Generated by Django 4.1.5 on 2023-01-24 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_rename_is_available_table_busy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='busy',
            field=models.BooleanField(default=False),
        ),
    ]
