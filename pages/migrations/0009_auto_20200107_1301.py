# Generated by Django 3.0.2 on 2020-01-07 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20200107_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='facebook',
            field=models.URLField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='location',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='contact',
            name='twitter',
            field=models.URLField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='youtube',
            field=models.URLField(max_length=255),
        ),
    ]
