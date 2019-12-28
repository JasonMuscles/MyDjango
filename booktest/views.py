from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import loader, RequestContext

# Create your views here.
# 1.定义一个视图,HttpResponse
# 2.进行url配置建立地址和视图的对应关系


def index(request):
    # M和T进行交互处理
    # return HttpResponse("老铁，没病")
    # 1.加载模板文件（路径相当对于是templates目录）
    temp = loader.get_template('booktest/index.html')

    # 2.定义一个模板上下文：给模板文件传递数据
    context = RequestContext(request, {})
    context.push(locals())

    # 3.模板渲染：产生标准的html的内容
    # res_html = temp.render(context)
    res_html = temp.render(context=locals(), request=request)

    # 4.返回给浏览器
    return HttpResponse(res_html)


def booktest(request):
    return HttpResponse("老铁，没毛病")
