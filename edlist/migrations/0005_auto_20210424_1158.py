# Generated by Django 3.1.6 on 2021-04-24 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edlist', '0004_auto_20210424_1030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='today',
            new_name='date',
        ),
    ]
