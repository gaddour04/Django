# Generated by Django 3.0.3 on 2020-05-10 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_cart_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='qty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.CartItem')),
            ],
        ),
    ]
