# Generated by Django 4.2.6 on 2023-11-01 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='prediction',
            field=models.BooleanField(default=False),
        ),
    ]
