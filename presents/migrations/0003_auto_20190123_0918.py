# Generated by Django 2.1.5 on 2019-01-23 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presents', '0002_auto_20190118_1418'),
    ]

    operations = [
        migrations.RenameField(
            model_name='giftpage',
            old_name='icon_back',
            new_name='icon',
        ),
        migrations.RemoveField(
            model_name='giftpage',
            name='icon_front',
        ),
    ]