# Generated by Django 2.2.1 on 2019-11-07 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0013_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='person',
            field=models.ManyToManyField(to='app01.Person'),
        ),
    ]
