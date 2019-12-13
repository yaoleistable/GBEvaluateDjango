# -*- coding: UTF-8 -*-
"""
@author: YaoLei
@file: urls.py
@time: 2019/12/13 16:13
"""
# index的urls
from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.index),
    # 添加带有字符类型、整型和slug的URL
    # path('<year>/<int:month>/<slug:day>', views.mydate),
    # 使用正则表达式，对输入内容进行限制
    re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2}).html', views.myDate),
    re_path('(?P<year>[0-9]{4}).html', views.myYear, name='myYear'),
    # 设置额外参数的，有bug
    re_path('(?P<year>[0-9]{4}).html', views.myYear_dict, {'month': '05'}, name='myYear_dict'),
]
