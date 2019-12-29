from django.conf.urls import url
from booktest import views

# url严格匹配开头和结尾
urlpatterns = [
    # 通过url函数设置url路由配置项
    url(r'^index$', views.index),   # 建立/index和视图index之间的关系
    url(r'^show_books$', views.show_books),  # 显示图书信息
    url(r'^books/(\d+)$', views.detail),  # 显示英雄信息
]
