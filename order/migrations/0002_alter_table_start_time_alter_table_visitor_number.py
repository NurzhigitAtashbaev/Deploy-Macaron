# Generated by Django 4.1.5 on 2023-01-24 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='visitor_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
