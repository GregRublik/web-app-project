# Generated by Django 4.2.6 on 2023-11-12 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_productbasket_count_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productbasket',
            name='numb_photo',
            field=models.CharField(default=None, max_length=20, verbose_name='Нумерация фото'),
        ),
    ]
