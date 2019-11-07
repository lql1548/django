from django.http import HttpResponse

def index(request):
    return HttpResponse("hello world")


from django.template import Template,Context
def tpltest(request):
    html="""
    <html>
    <head></head>
    <body>
    <h1>这是一个tpltest页面</h1>
    <h2>姓名:{{ name }}</h2>
    </body>
    </html>
    """
    # 数据的渲染
    name = "老张"
    # 1.实例化一个 template 对象
    template_obj = Template(html)

    context_obj = Context()
    return HttpResponse(html)

from django.shortcuts import render,render_to_response
def myindex(request):
    return render(request,"index.html",{"name":"laowang"})

def myindex2(request):
    return render_to_response("index.html",{"name":"index2"})

from datetime import datetime
def tmptest(request):
    name = "hello"
    age = 18
    hobby = ["sing","football","dance","play"]
    score = {"yuwen":100,"shuxue":120,"yingyu":122}
    now_time = datetime.now()
    # now_time = now_time.strftime("%Y-%m-%d %H:%M:%S")
    js = """
    <script>
        alert("111111");
    </script>
    """
    return render(request,"tmptest.html",locals())

def statictest(request):
    return render(request,"statictest.html")