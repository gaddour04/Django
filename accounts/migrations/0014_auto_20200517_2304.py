# Generated by Django 3.0.3 on 2020-05-17 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_contact_countryphone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='countryphone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
