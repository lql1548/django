# Generated by Django 2.2.1 on 2019-11-05 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=4)),
            ],
        ),
    ]
