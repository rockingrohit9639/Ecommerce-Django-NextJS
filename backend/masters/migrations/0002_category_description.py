# Generated by Django 3.2.8 on 2021-10-07 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
