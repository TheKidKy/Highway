# Generated by Django 4.0.6 on 2022-07-30 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_module', '0010_alter_post_tag_postvisit'),
    ]

    operations = [
        migrations.AddField(
            model_name='posttag',
            name='posts',
            field=models.ManyToManyField(to='blog_module.post', verbose_name='Posts'),
        ),
    ]
