# Generated by Django 4.1.1 on 2022-10-05 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_module', '0022_alter_postcomment_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='comment',
            field=models.TextField(),
        ),
    ]