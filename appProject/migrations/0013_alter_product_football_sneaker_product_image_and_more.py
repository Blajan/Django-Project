# Generated by Django 4.1.1 on 2022-09-16 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProject', '0012_rename_date_product_football_sneaker_product_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_football_sneaker',
            name='product_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='product_hat',
            name='product_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='product_pant',
            name='product_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='product_sneakers',
            name='product_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='product_t_shirt',
            name='product_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics'),
        ),
    ]
