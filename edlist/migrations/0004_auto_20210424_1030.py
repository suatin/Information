# Generated by Django 3.1.6 on 2021-04-24 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edlist', '0003_item_today'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='today',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]