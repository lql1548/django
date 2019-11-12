"""ArticleBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^$',index),
    path('about/', about),
    path('index/', index),
    path('listpic/', listpic),
    path('newslistpic/', newslistpic),
    re_path('newslistpic/(?P<page>\d+)/', newslistpic),
    path('base/', base),
    # path('articleDetail/', articleDetail),
    re_path('articleDetail/(?P<id>\d+)/', articleDetail),
    path('fytest/', fytest),
    path('ckeditor/', include("ckeditor_uploader.urls")),
    path('requesttest/', requesttest),
    path('reqtest/', reqtest),
    path('search/', search),
    path('reqpost/', reqpost),
    path('register/', register),
    path('ajaxtest/', ajaxtest),
    path('ajaxdemo/', ajaxdemo),
    path('ajaxreq/', ajaxreq),
    path('ajaxregister/', ajaxregister),
    path('ajaxpost/', ajaxpost),
    path('Article/', include("Article.urls")),
]
