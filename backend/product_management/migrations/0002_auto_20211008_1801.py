# Generated by Django 3.2.8 on 2021-10-08 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
