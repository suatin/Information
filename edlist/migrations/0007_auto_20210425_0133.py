# Generated by Django 3.1.6 on 2021-04-25 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edlist', '0006_auto_20210424_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='concern',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='suggest',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
