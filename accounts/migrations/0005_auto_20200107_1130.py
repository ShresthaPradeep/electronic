# Generated by Django 3.0.2 on 2020-01-07 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20200106_1218'),
        ('accounts', '0004_auto_20200107_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favourite',
            name='product',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='favourite_product', to='products.Product'),
        ),
    ]