# Generated by Django 4.1.4 on 2022-12-21 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0002_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null='True', upload_to='posteos'),
            preserve_default='True',
        ),
    ]