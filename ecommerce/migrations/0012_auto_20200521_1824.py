# Generated by Django 3.0.3 on 2020-05-21 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0011_auto_20200521_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color1',
            field=models.CharField(choices=[('red', 'red'), ('noir', 'noir')], max_length=100, verbose_name='Color '),
        ),
    ]
