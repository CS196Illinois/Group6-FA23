# Generated by Django 4.2.5 on 2023-10-27 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databaseapp', '0005_alter_stock_stock_date_alter_stock_stock_ticker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='stock_date',
            field=models.TextField(default=0),
        ),
    ]