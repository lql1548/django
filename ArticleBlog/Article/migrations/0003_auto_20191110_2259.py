# Generated by Django 2.2.1 on 2019-11-10 14:59

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0002_article_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='click',
            field=models.IntegerField(default=0, verbose_name='点击率'),
        ),
        migrations.AddField(
            model_name='article',
            name='recommend',
            field=models.IntegerField(default=0, verbose_name='推荐'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
