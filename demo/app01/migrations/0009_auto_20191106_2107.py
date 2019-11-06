# Generated by Django 2.2.1 on 2019-11-06 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_user_height'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='书名')),
            ],
        ),
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='出版社')),
                ('address', models.TextField(verbose_name='地址')),
            ],
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=4, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='user',
            name='height',
            field=models.DecimalField(decimal_places=2, default=176, max_digits=5, verbose_name='身高'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=32, verbose_name='姓名'),
        ),
    ]
