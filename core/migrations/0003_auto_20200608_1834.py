# Generated by Django 2.2 on 2020-06-08 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_orderitem_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
