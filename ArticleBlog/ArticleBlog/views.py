from django.http import HttpResponse
from django.shortcuts import render
from Article.models import *
from django.core.paginator import Paginator

def about(request):
    return render(request,"about.html")

def index(request):
    """
    返回  最新的  6条数据
    返回图文推荐  7条数据
    返回点击排行  12条数据

    :param request:
    :return:
    """
    newarticle = Article.objects.order_by("-date")[:6]
    # 返回图文推荐  7条数据
    recommendArticle = Article.objects.filter(recommend=1)[:7]
    # 返回点击率
    clickArticle = Article.objects.order_by("-click")[:12]

    return render(request,"index.html",locals())
def listpic(request):
    return render(request,"listpic.html")


def newslistpic(request,page=1):
    page = int(page)
    # 查询数据
    article = Article.objects.all().order_by("id")
    # 返回数据
    paginator = Paginator(article,6)  ## 每页显示六条数据
    page_obj = paginator.page(page)

    # page_range = paginator.page_range[:5]
    # 获取当前页数
    number = page_obj.number
    # start = number - 3
    # end = number + 2
    if number <=2:
        start = 0
        end = 5
    elif number >=paginator.num_pages -2:
        end = paginator.num_pages
        start = end - 5
    else:
        start = number - 3
        end = number + 2
    page_range = paginator.page_range[start:end]
    return render(request,"newslistpic.html",locals())

def base(request):
    return render(request,"base.html")

# 文章详情
def articleDetail(request,id):
    id = int(id)
    article = Article.objects.filter(id=id).first()
    article.click += 1
    article.save()
    return render(request,"articleDetail.html",locals())


def fytest(request):
    article = Article.objects.all()

    paginator = Paginator(article,6)
    # print(paginator.num_pages)  ## 总页数
    # print(paginator.page_range)  ## 页码范围

    page_obj = paginator.page(10)
    print(page_obj.next_page_number())
    print(page_obj.previous_page_number())
    # print(page_obj.has_next())
    # print(page_obj.has_previous())
    # print(page_obj)
    # for one in page_obj:
    #     print(one)
        # print(one.title)
    return HttpResponse("分页")

def requesttest(request):
    # print(dir(request))
    # print(request.COOKIES)  ## 用户的身份
    # print(request.FILES)  ## 请求携带的文件  比如：图片，文档，压缩包
    # print(request.META)  ## 请求的具体数据，包含所有的http请求信息
    # print(request.GET)  ## 获取get请求传递的参数
    # print(request.GET.get("name"))  ## 获取get请求参数中 指定key的value
    # print(request.POST)  ##　获取post请求传递的参数
    # print(request.POST.get("name"))  ## 获取post请求参数中指定key的value
    # print(request.scheme)  ##  http 或者是  https
    # print(request.method)  ## 获取请求方式  POST  GET
    # print(request.path)  ##　请求的路径
    # print(request.body)  ## 请求的主体，放请求的内容  bytes 类型
    # print(request.META.get("OS"))  ##请求来源使用的操作系统
    # print(request.META.get("HTTP_USER_AGENT"))  ## 浏览器的版本
    # print(request.META.get("HTTP_HOST"))  ## 请求的主机
    # print(request.META.get("HTTP_REFERER"))  ## 请求的来源
    return HttpResponse("请求demo")

def reqtest(request):
    # 获取get请求的参数
    data = request.GET
    print(data)
    username = request.GET.get("uname")
    password = request.GET.get("pwd")
    print(username)
    print(password)
    return render(request,"reqtest.html")


def search(request):
    # 获取数据
    search_key = request.GET.get("searchkey")
    # 判断是否空值
    if search_key:
        # 如果有数据  查询数据库
        article = Article.objects.filter(title__icontains=search_key).all().values("title")
    # 如果没有数据  返回页面
    return render(request,"search.html",locals())

import hashlib
# 加密
def setPassword(password):
    # 将password  通过md5 加密
    md5 = hashlib.md5()
    md5.update(password.encode())  ## 要求，传递的是一个 bytes类型
    result = md5.hexdigest()
    return result

from Article.form import UserForm
# 用户注册
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # 判断是否为空值
        if username and password:
            flag = User.objects.filter(name=username).first()
            # 用户不存在
            if not flag:
                user = User()
                user.name = username
                user.password = setPassword(password)
                user.save()
                result = "注册成功"
            else:
                result = "用户已存在"
        else:
            result = "用户名或密码为空"
    return render(request,"register.html",locals())

def reqpost(request):
    # 接收用户的请求
    if request.method == "POST":
        # 处理页面
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username)
        print(password)
    return render(request,"reqpost.html")


def ajaxtest(request):
    return render(request,"ajaxtest.html",locals())


# 提供页面
def ajaxdemo(request):
    return render(request,"ajaxdemo.html")

from django.http import JsonResponse
# 处理ajax请求
def ajaxreq(request):
    """
    接收用户的请求   校验用户名  密码
        参数：  username  password
    处理请求
        查询数据库  查看指定用户名密码的用户是否存在
    返回响应
        存在或者  不存在
    :param request:
    :return:
    """
    print(request.GET)
    username = request.GET.get("username")
    password = request.GET.get("password")
    result = {"code":10000,"msg":""}
    if username and password:
        flag = User.objects.filter(name=username,password=setPassword(password)).first()
        if flag:
            result["msg"]= "存在"
        else:
            result["msg"]= "不存在"
            result["code"]=10001
    else:
        result["msg"] = "用户名或者密码为空"
        result["code"] = 10002
    return JsonResponse(result)

# 提供注册页面
def ajaxregister(request):
    return render(request,"ajaxregister.html")
# 处理ajax请求
def ajaxpost(request):
    result = {"code": 10000, "msg": ""}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            flag = User.objects.filter(name=username,password=setPassword(password)).first()
            if flag:
                result["msg"]="用户已存在"
                result["code"]=10001
            else:
                User.objects.create(name=username,password=setPassword(password))
                result["msg"]="注册成功"
        else:
            result["msg"]="用户名或密码为空"
            result["code"]=10002
    return JsonResponse(result)