# Generated by Django 3.0.3 on 2020-05-22 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0006_auto_20200522_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='reduction',
            field=models.DecimalField(decimal_places=2, max_digits=65),
        ),
    ]