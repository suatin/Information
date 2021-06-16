# Generated by Django 3.1.6 on 2021-06-14 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edlist', '0003_auto_20210610_1641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memberdetails',
            old_name='M_name',
            new_name='M_firstname',
        ),
        migrations.RenameField(
            model_name='officerdetails',
            old_name='name',
            new_name='contactnumber',
        ),
        migrations.AddField(
            model_name='memberdetails',
            name='M_contactnumber',
            field=models.EmailField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='memberdetails',
            name='M_middlename',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='memberdetails',
            name='M_section',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='memberdetails',
            name='M_surname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='officerdetails',
            name='firstname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='officerdetails',
            name='middlename',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='officerdetails',
            name='section',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='officerdetails',
            name='surname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='activitiesdetails',
            name='estimated_Budget',
            field=models.IntegerField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='activitiesdetails',
            name='paticipant_number',
            field=models.IntegerField(default=0, max_length=20),
        ),
    ]
