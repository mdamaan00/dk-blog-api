# Generated by Django 3.2.12 on 2022-03-29 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_api', '0003_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=None, upload_to='blog'),
        ),
    ]
