# Generated by Django 3.0.2 on 2020-01-12 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_product_views'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='views',
            new_name='view_count',
        ),
    ]
