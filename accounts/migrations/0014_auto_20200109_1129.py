# Generated by Django 3.0.2 on 2020-01-09 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20200109_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.ManyToManyField(to='accounts.CartProduct'),
        ),
    ]