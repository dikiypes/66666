# Generated by Django 4.2.7 on 2024-01-14 17:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_category_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='create_date',
            field=models.DateField(default=datetime.date(2024, 1, 14), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='update_date',
            field=models.DateField(default=datetime.date(2024, 1, 14), verbose_name='Дата последнего изменения'),
        ),
    ]