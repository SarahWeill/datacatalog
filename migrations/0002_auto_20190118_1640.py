# Generated by Django 2.1.4 on 2019-01-18 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacatalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='keywords',
            field=models.ManyToManyField(to='datacatalog.Keyword'),
        ),
        migrations.AlterField(
            model_name='datauseagreement',
            name='users',
            field=models.ManyToManyField(to='persons.Person'),
        ),
    ]
