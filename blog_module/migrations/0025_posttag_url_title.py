# Generated by Django 4.1.1 on 2022-11-02 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_module', '0024_rename_comment_postcomment_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='posttag',
            name='url_title',
            field=models.CharField(db_index=True, max_length=20, null=True),
        ),
    ]
