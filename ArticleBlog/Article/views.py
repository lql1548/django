from django.shortcuts import render
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from .models import *
from ArticleBlog.views import setPassword

# Create your views here.
def checkuser(request):
    result = {"code":10000,"msg":""}
    # 校验用户名是否存在
    username = request.GET.get("username")
    if username:
        user = User.objects.filter(name=username).first()
        if user:
            result = {"code":10001,"msg":"用户名存在"}
        else:
            result = {"code":10000,"msg":"用户名可用"}
    else:
        result = {"code":10002,"msg":"参数为空"}
    return JsonResponse(result)

