# Generated by Django 3.0 on 2020-05-27 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20190330_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='catimage',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
    ]
