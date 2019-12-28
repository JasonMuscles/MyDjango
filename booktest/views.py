from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
# 1.定义一个视图,HttpResponse
# 2.进行url配置建立地址和视图的对应关系


def index(request):
    # M和T进行交互处理
    return HttpResponse("老铁，没病")


def booktest(request):
    return HttpResponse("老铁，没毛病")
