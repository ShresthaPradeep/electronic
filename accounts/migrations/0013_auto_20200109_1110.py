# Generated by Django 3.0.2 on 2020-01-09 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_cartproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='color',
            field=models.CharField(default='White', max_length=150),
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
