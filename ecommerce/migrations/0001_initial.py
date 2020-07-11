# Generated by Django 3.0.3 on 2020-04-09 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_prod', models.CharField(max_length=40)),
                ('prix', models.IntegerField()),
                ('image', models.ImageField(upload_to='ecommerce/static/ecommerce/images')),
            ],
        ),
    ]
