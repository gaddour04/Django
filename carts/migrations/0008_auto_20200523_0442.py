# Generated by Django 3.0.3 on 2020-05-23 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0007_auto_20200522_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='reduction',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=65),
        ),
    ]
