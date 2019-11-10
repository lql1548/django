from django.http import HttpResponse
from django.shortcuts import render
from Article.models import *
from django.core.paginator import Paginator

def about(request):
    return render(request,"about.html")
def index(request):
    return render(request,"index.html")
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
