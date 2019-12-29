# -*- coding: UTF-8 -*-
"""
@author: YaoLei
@file: urls.py
@time: 2019/12/13 16:13
"""
# index的urls
from django.urls import path, re_path

from . import views

urlpatterns = {
    # ^表示以form开头，$表示以/结尾
    path('', views.getform),
}
