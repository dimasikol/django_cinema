# Generated by Django 4.2.13 on 2024-07-13 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinema',
            name='preview_image',
            field=models.ImageField(upload_to='cinema/%Y/%m/%d/', verbose_name='image'),
        ),
    ]