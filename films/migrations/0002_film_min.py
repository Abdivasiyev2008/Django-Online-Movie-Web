# Generated by Django 4.2.2 on 2023-06-16 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='min',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]