# Generated by Django 3.0.3 on 2020-05-21 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0010_auto_20200516_0127'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color1',
            field=models.BooleanField(default=True, verbose_name='Color noir'),
        ),
        migrations.AddField(
            model_name='product',
            name='color2',
            field=models.BooleanField(default=False, verbose_name='Color noir'),
        ),
        migrations.AddField(
            model_name='product',
            name='color3',
            field=models.BooleanField(default=False, verbose_name='Color noir'),
        ),
        migrations.AddField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='Image 1'),
        ),
        migrations.AddField(
            model_name='product',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='Image 2'),
        ),
        migrations.AddField(
            model_name='product',
            name='image6',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='Image 3'),
        ),
        migrations.AddField(
            model_name='product',
            name='image7',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='Image 1'),
        ),
        migrations.AddField(
            model_name='product',
            name='image8',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='Image 2'),
        ),
        migrations.AddField(
            model_name='product',
            name='image9',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='Image 3'),
        ),
    ]
