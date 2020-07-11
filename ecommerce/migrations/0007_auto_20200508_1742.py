# Generated by Django 3.0.3 on 2020-05-08 16:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecommerce', '0006_product_favourite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='favourite',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='favourite', to=settings.AUTH_USER_MODEL),
        ),
    ]