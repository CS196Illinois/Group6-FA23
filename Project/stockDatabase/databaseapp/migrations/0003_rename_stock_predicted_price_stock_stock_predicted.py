# Generated by Django 4.2.5 on 2023-10-06 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('databaseapp', '0002_alter_stock_stock_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='stock_predicted_price',
            new_name='stock_predicted',
        ),
    ]