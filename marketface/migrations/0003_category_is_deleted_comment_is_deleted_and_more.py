# Generated by Django 5.0 on 2023-12-15 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketface', '0002_alter_comment_image_alter_product_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comment',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productabout',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='type',
            name='image',
            field=models.ImageField(default=1, upload_to='type_image/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='type',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='category_image/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='product_image/'),
        ),
    ]
