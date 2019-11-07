from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
    return HttpResponse("我是子应用index页面")

def addUser(request):
    return HttpResponse("增加数据")

def getData(request):
    # all()
    # 返回 queryset
    # data = User.objects.all()
    # print(data)

    # get()
    # 返回  object  有且只有一条数据
    # data = User.objects.get(id=4)
    # # data = User.objects.get(id=2)  ## 数据不存在  报错
    # # data = User.objects.get(name="lisi")  ## 报错
    # print(data)

    # filter()
    # 返回 queryset  select * from user where gender="1";
    # data = User.objects.filter(gender='1')
    # print(data)

    # first()
    # 返回 object  返回符合条件的第一条数据
    # data = User.objects.all().first()
    # print(data)

    # last()
    # 返回  object 符合条件的最后一条数据
    # data = User.objects.all().last()
    # print(data)

    # exclude()
    # 返回  queryset
    # data = User.objects.exclude(name="lisi")
    # print(data)

    # order_by()
    # 返回  queryset
    # 正序
    # data = User.objects.all().order_by("id")
    # print(data)
    # 降序
    # data2 = User.objects.all().order_by("-id")
    # print(data2)
    # reverse()

    # values()
    # 返回 queryset   object 没有 values()方法
    # data = User.objects.all().values("name","id")
    # print(data)

    # exists()
    # 返回  布尔值 True False
    # data = User.objects.filter(name="lisi").exists()
    # print(data)  # True
    # data = User.objects.filter(name="libai").exists()
    # print(data)  # False

    # count()  计数
    # data = User.objects.all().count()
    # print(data)

    # 切片 [1:10]
    data = User.objects.all()[1:3]
    print(data)

    return render(request,"getData.html",locals())

def updateUser(request):
    # 1.save()
    # data = User.objects.get(id=9)
    # data.age=30
    # data.save()

    # data = User.objects.filter(name="lisi")
    # for one in data:
    #     one.name="python"
    #     one.save()

    # 2.update()
    User.objects.filter(name="lisi",age=24).update(age=22)
    return HttpResponse("修改数据")
def deleteUser(request):
    return HttpResponse("删除数据")

def doubleLine(request):
    # __lt 小于
    # data = User.objects.filter(age__lt=24)  # age 小于 24
    # __lte 小于等于
    # data = User.objects.filter(age__lte=24)
    # __gt 大于
    # data = User.objects.filter(age__gt=24)  # age 大于 24
    # __gte 大于等于
    # data = User.objects.filter(age__gte=24)
    # __in  包含
    # data = User.objects.filter(id__in=[1,2,5,7,9]).values("id")
    # __contains
    # data = User.objects.filter(name__contains="j").values("name")  # contains 大小写敏感
    # date = User.objects.filter(name__icontains="j").values("name")  # icontains 大小写不敏感
    # __startswith
    # data = User.objects.filter(name__startswith="w").values("name") # 以指定字符开头  大小写敏感
    # date = User.objects.filter(name__istartswith="w").values("name") # 以指定字符开头  大小写不敏感
    # __range
    data = User.objects.filter(id__range=(7,10))
    date = User.objects.exclude(id__range=(7,10))
    return render(request,"doubleLine.html",locals())

def OneToManyAdd(request):
    # 增加数据
    # 先增加 publish 表数据
    # Publish.objects.create(name="北京出版社",address="北京")
    # Publish.objects.create(name="山东出版社",address="山东")
    # Publish.objects.create(name="中公出版社",address="中公")

    # 增加 book 数据
    # 第一种
    # Book.objects.create(name="python基础",publish_id=1)
    # 第二种
    # publish = Publish.objects.get(name="北京出版社")
    # Book.objects.create(name="python开发",publish_id=publish.id)
    # 第三种
    # publish = Publish.objects.get(name="山东出版社")
    # Book.objects.create(name="pythonWeb",publish=publish)
    # 第四种
    # Book.objects.create(name="pythonWeb",publish=Publish.objects.get(name="中公出版社"))

    # 正向 从外键所在表到关联表的操作叫正向操作
    # book = Book()
    # book.name="python数据分析"
    # book.publish=Publish.objects.get(name="中公出版社")
    # book.save()

    # 反向 从关联表到外键所在的表的操作叫反向操作
    # publish_obj = Publish.objects.get(name="中公出版社")
    # publish_obj.book_set.create(name="python爬虫")

    # publish_obj = Publish.objects.create(name="东北出版社",address="东北")
    # publish_obj.book_set.create(name="python技术")
    return HttpResponse("一对多添加数据")

def OneToManyGet(request):
    # 查询
    # 查询 北京出版社的书籍
    # pub_obj = Publish.objects.get(name="北京出版社")
    # book_obj = Book.objects.filter(publish=pub_obj).values("name")
    # print(book_obj)

    # 查询 python基础的出版社名字
    # book = Book.objects.get(name="python基础")
    # pub = Publish.objects.get(id=book.publish_id)
    # print(pub.name)

    # 正向查询
    # 查 python基础 属于哪个出版社
    # book = Book.objects.filter(name="python基础").first()
    # pubname = book.publish.name
    # print(pubname)
    # pub = book.publish
    # print(pub)  # Publish object (1)

    # 反向查询
    # 查北京出版社的书
    # pub = Publish.objects.filter(name="北京出版社").first()
    # book = pub.book_set.all().values("name")
    # print(book)

    # 查询 北京出版社 出版的 python基础
    # pub = Publish.objects.filter(name="北京出版社").first()
    # book = pub.book_set.filter(name="python基础").values()
    # print(book)

    # 查询 python基础的出版社出版的所有书籍
    # 1.查询 python基础的出版社
    # 2.查询这个出版社出版的所有书籍
    # book = Book.objects.get(name="python基础")
    # pub = book.publish  # 出版社
    # book_all = pub.book_set.values()
    # print(book_all)
    # book_all = Book.objects.get(name="python基础").publish.book_set.values()
    return render(request,"OneToManyGet.html",locals())

def OneToManyUpdate(request):
    # save  将 Python基础的出版社  修改为 山东出版社
    # book = Book.objects.filter(name="python基础").first()
    # pub = Publish.objects.filter(name="山东出版社").first()
    # book.publish = pub
    # book.save()

    # update()
    # pub = Publish.objects.get(name="山东出版社")
    # Book.objects.filter(name="python基础").update(publish=pub)

    # 反向
    # 给 北京出版社 增加好多本书
    # pub = Publish.objects.get(name="北京出版社")
    # book = Book.objects.get(name="python爬虫")
    # book1 = Book.objects.get(name="python技术")
    # pub.book_set.set([book,book1])
    return HttpResponse("一对多修改数据")

def OneToManyDelete(request):
    # 先删除外键所在的表
    # Book.objects.filter(name="python基础").first().delete()
    # 删除关联表
    # book = Book.objects.filter(name="pythonWeb").first()
    # book.delete()
    #
    # Publish.objects.filter(id = book.publish_id).delete()
    return HttpResponse("一对多删除")

def ManyAdd(request):
    # 增加老师
    # Teacher.objects.create(name="老王",gender=1)
    # Teacher.objects.create(name="老刘",gender=1)
    # Teacher.objects.create(name="老边",gender=1)
    # Teacher.objects.create(name="老张",gender=1)
    # Teacher.objects.create(name="小丽",gender=0)

    # 增加 person
    # Person.objects.create(name="小王",age=17,height=170)

    # 正向操作
    # 小二 想学老刘的课
    # teacher = Teacher.objects.filter(name="老刘").first()
    # teacher.person.create(name="小二",age=20,height=168)

    # 小三 和 小四 想学 女老师的课
    # teacher = Teacher.objects.filter(gender=0).first()
    # person = Person.objects.create(name="小三",age=19,height=188)
    # person1 = Person.objects.create(name="小四",age=20,height=169)
    # teacher.person.add(person,person1)

    # 反向操作
    # 小五 想学老王的课程
    # person = Person.objects.create(name="小五",age=20,height=170)
    # teacher = Teacher.objects.filter(name="老王").first()
    # person.teacher_set.add(teacher)

    return HttpResponse("多对多添加数据")

def ManyGet(request):
    # 正向
    # 查询 小丽老师的学生
    # teacher = Teacher.objects.filter(name="小丽").first()
    # person = teacher.person.all().values("name")
    # print(person)

    # 反向
    # 查询  小三的老师
    # person = Person.objects.filter(name="小三").first()
    # teacher = person.teacher_set.all().values("name")
    # print(teacher)
    return HttpResponse("多对多查询数据")

def ManyUpdate(request):
    # 正向
    # 添加小三 小四  小五为 老刘的学生
    # teacher = Teacher.objects.filter(name="老刘").first()
    # teacher.person.set([3,4,5])

    # 反向
    # 给小三添加老师
    person = Person.objects.get(name="小三")
    person.teacher_set.set([1,2,3,4])
    # person.teacher_set.set([p1,p2,p3,p4])
    return HttpResponse("多对多修改数据")

def ManyDelete(request):
    # remove  解除关系
    # 解除小四和小丽的关系
    # 正向
    # teacher = Teacher.objects.filter(name="小丽").first()
    # person = Person.objects.filter(name="小四").first()
    # teacher.person.remove(person)

    # 反向
    # person = Person.objects.filter(name="小三").first()
    # teacher = Teacher.objects.filter(name="小丽").first()
    # person.teacher_set.remove(teacher)


    # clear  清空
    # 反向  删除小五的所有关系
    # person = Person.objects.filter(name="小五").first()
    # person.teacher_set.clear()

    # 正向  删除老刘的所有关系
    # teacher = Teacher.objects.filter(name="老刘").first()
    # teacher.person.clear()

    # delete  删除数据
    Person.objects.filter(name="小三").delete()
    return HttpResponse("多对多删除数据")


from django.db.models import Sum,Avg,Count,Max,Min
def juhe(request):
    # data = Person.objects.all().aggregate(Count("id"),Count("name"))
    data = Person.objects.all().aggregate(Count("id"))
    print(data)
    print(data["id__count"])
    return HttpResponse("聚合函数")