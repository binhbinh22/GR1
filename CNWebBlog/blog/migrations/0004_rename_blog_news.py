# Generated by Django 4.0.1 on 2023-07-22 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_delete_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog',
            new_name='News',
        ),
    ]