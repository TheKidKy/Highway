# Generated by Django 4.0.4 on 2022-06-08 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_module', '0002_alter_post_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, default='', editable=False, unique=True),
        ),
    ]
