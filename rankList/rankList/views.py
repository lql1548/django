from django.http import HttpResponse
from django.shortcuts import render

def base(request):
    urldata = [
        {"name":"白宇","img":"by.jpg"},
        {"name":"周渝民","img":"zym.jpg"},
        {"name":"马天宇","img":"mty.jpg"},
        {"name":"魏大勋","img":"wdx.jpg"},
    ]
    return render(request,"base.html",locals())