# Generated by Django 3.1.4 on 2020-12-28 13:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20201228_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_file',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
