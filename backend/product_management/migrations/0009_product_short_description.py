# Generated by Django 3.2.8 on 2021-10-11 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_management', '0008_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
