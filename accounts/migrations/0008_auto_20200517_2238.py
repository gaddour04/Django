# Generated by Django 3.0.3 on 2020-05-17 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200517_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
