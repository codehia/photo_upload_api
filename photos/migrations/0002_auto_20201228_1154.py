# Generated by Django 3.1.4 on 2020-12-28 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Albums',
            new_name='Album',
        ),
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
    ]