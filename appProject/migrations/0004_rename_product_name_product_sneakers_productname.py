# Generated by Django 4.1.1 on 2022-09-12 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appProject', '0003_product_football_sneaker_product_hat_product_pant_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_sneakers',
            old_name='product_name',
            new_name='productName',
        ),
    ]
