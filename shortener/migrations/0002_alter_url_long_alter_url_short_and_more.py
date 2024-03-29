# Generated by Django 5.0 on 2024-02-17 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='long',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='short',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='short_viewed',
            field=models.IntegerField(default=0),
        ),
    ]
