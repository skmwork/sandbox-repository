# Generated by Django 3.0.4 on 2020-05-01 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/products/%Y/%m/%d'),
        ),
    ]
