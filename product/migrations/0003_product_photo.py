# Generated by Django 4.1.5 on 2023-02-02 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_image_options_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]