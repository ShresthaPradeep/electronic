# Generated by Django 3.0.2 on 2020-01-07 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20200107_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='country_code',
            field=models.CharField(default='', max_length=3),
        ),
    ]