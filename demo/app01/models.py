from django.db import models

# Create your models here.
class User(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32,verbose_name="姓名")
    age = models.IntegerField(verbose_name="年龄")
    gender = models.CharField(max_length=4,verbose_name="性别")
    height = models.DecimalField(max_digits=5,decimal_places=2,default=176,verbose_name="身高")
    # def __str__(self):
    #     return self.name

    class Meta:
        db_table = 'user'
        # ordering = ["-id"]
        verbose_name = "用户"
        verbose_name_plural = verbose_name


class Publish(models.Model):
    name = models.CharField(max_length=32,verbose_name="出版社")
    address = models.TextField(verbose_name="地址")
    class Meta:
        db_table = "publish"


class Book(models.Model):
    name = models.CharField(max_length=32,verbose_name="书名")
    publish = models.ForeignKey(to=Publish,on_delete=models.CASCADE)
    class Meta:
        db_table = "book"


class Person(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    height = models.FloatField()
    birthday = models.DateField(auto_now=True)
    class Meta:
        db_table = "person"

GENDER_LIST = (
    (0,"女"),
    (1,"男")
)
class Teacher(models.Model):
    name = models.CharField(max_length=32)
    gender = models.IntegerField(choices=GENDER_LIST)
    person = models.ManyToManyField(to=Person)
    class Meta:
        db_table = "teacher"