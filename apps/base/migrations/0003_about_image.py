# Generated by Django 5.1 on 2024-09-10 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_about_options_alter_about_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='image',
            field=models.ImageField(default=1, upload_to='about_images/', verbose_name='Фотография'),
            preserve_default=False,
        ),
    ]
