# Generated by Django 2.1.5 on 2019-01-23 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presents', '0003_auto_20190123_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='giftpage',
            name='icon_url',
            field=models.TextField(blank=True),
        ),
    ]
