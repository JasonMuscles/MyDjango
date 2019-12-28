from django.conf.urls import url
from booktest import views

urlpatterns = [
    # 通过url函数设置url路由配置项
    url(r'^index', views.index),   # 建立/index和视图index之间的关系
    url(r'^booktest', views.booktest),
]
