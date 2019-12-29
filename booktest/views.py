from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import loader, RequestContext
from booktest.models import BookInfo  # 导入图书

# Create your views here.
# 1.定义一个视图,HttpResponse
# 2.进行url配置建立地址和视图的对应关系


# def my_render(request, template_path, context_dict={}):
#     # 1.加载模板文件（路径相当对于是templates目录）
#     temp = loader.get_template(template_path)
#
#     # 2.定义一个模板上下文：给模板文件传递数据
#     context = RequestContext(request, context_dict)
#     context.push(locals())
#
#     # 3.模板渲染：产生标准的html的内容
#     # res_html = temp.render(context)
#     res_html = temp.render(context=locals(), request=request)
#
#     # 4.返回给浏览器
#     return HttpResponse(res_html)


def index(request):
    # M和T进行交互处理
    # return HttpResponse("老铁，没病")
    return render(request, 'booktest/index.html', {'content': 'Hello World',
                  'list': list(range(1, 10))})


def show_books(request):
    """显示图书的信息"""
    # 1.通过M查找图书表中的数据
    books = BookInfo.objects.all()
    # 2.使用模板
    return render(request, 'booktest/show_books.html', {'books': books})


def detail(request, bid):
    """根据图书关联英雄"""
    # 1.根据bid查询图书信息
    book = BookInfo.objects.get(id=bid)
    # 2.查询和book关联的英雄信息
    heros = book.heroinfo_set.all()
    # 3.使用模板
    return render(request, 'booktest/detail.html', {'book': book, 'heros': heros})