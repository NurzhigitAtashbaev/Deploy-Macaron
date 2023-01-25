# Generated by Django 4.1.5 on 2023-01-24 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('seats', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('visitor_name', models.CharField(blank=True, max_length=100, null=True)),
                ('visitor_number', models.IntegerField()),
                ('message', models.TextField(blank=True, max_length=2000, null=True)),
                ('start_time', models.DateTimeField()),
            ],
        ),
    ]