# Generated by Django 2.2.1 on 2019-11-05 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_remove_user_height'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='height',
            field=models.DecimalField(decimal_places=2, default=176, max_digits=5),
            preserve_default=False,
        ),
    ]
