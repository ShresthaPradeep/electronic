# Generated by Django 3.0.2 on 2020-01-13 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartproduct',
            name='checked_out',
        ),
        migrations.AddField(
            model_name='cart',
            name='checked_out',
            field=models.BooleanField(default=False),
        ),
    ]