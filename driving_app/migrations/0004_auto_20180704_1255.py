# Generated by Django 2.0.6 on 2018-07-04 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driving_app', '0003_auto_20180704_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='adress',
            field=models.TextField(help_text='Nayabazar,kathmandu'),
        ),
    ]