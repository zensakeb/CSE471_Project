# Generated by Django 5.2 on 2025-05-03 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_rename_image_project_image_url_remove_project_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image_url',
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='project_images/'),
        ),
    ]
