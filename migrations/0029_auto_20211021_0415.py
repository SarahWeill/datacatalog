# Generated by Django 3.2 on 2021-10-21 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacatalog', '0028_auto_20211021_0132'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataaccess',
            name='data_retained',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dataaccess',
            name='retention_requested',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
