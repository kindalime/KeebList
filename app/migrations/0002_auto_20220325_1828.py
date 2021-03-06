# Generated by Django 3.2.5 on 2022-03-25 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessory',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='accessory',
            name='slug',
            field=models.SlugField(default='9zx8Yy7ypJ', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='artisan',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='artisan',
            name='slug',
            field=models.SlugField(default='9zx8Yy7ypJ', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='build',
            name='slug',
            field=models.SlugField(default='9zx8Yy7ypJ', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='keyboard',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='keyboard',
            name='slug',
            field=models.SlugField(default='9zx8Yy7ypJ', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='keycap',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='keycap',
            name='production',
            field=models.CharField(blank=True, choices=[('Doubleshot', 'Doubleshot'), ('Tripleshot', 'Tripleshot'), ('Dye-Sublimated', 'Dye-Sublimated'), ('Other', 'Other')], max_length=255),
        ),
        migrations.AlterField(
            model_name='keycap',
            name='slug',
            field=models.SlugField(default='9zx8Yy7ypJ', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='switch',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='switch',
            name='slug',
            field=models.SlugField(default='9zx8Yy7ypJ', max_length=255, unique=True),
        ),
    ]
