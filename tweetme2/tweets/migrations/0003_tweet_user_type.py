# Generated by Django 2.2 on 2021-11-30 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_tweet_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='user_type',
            field=models.CharField(choices=[('U', 'User'), ('A', 'Administrator')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
