# Generated by Django 4.2.5 on 2023-10-12 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databaseapp', '0004_rename_stock_name_stock_stock_ticker_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='stock_date',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stock',
            name='stock_ticker',
            field=models.TextField(default=''),
        ),
    ]
