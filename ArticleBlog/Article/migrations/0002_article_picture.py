# Generated by Django 2.2.1 on 2019-11-10 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='picture',
            field=models.ImageField(default='images/01.jpg', upload_to='images'),
            preserve_default=False,
        ),
    ]
