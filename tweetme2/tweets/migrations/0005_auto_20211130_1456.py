# Generated by Django 2.2 on 2021-11-30 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_auto_20211130_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='date_joined',
            field=models.DateField(auto_now_add=True),
        ),
    ]
