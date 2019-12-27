# -*- coding: UTF-8 -*-
"""
@author: YaoLei
@file: adminx.py
@time: 2019/12/27 10:35
"""
import xadmin
from .models import School


class SchoolAdmin(object):
    # pass
    # 显示的字段
    list_display = ['name', 'address']
    # 每页显示多少个
    list_per_page = 20
    # 搜索
    search_fields = ['name', 'address']
    # 过滤器
    list_filter = ['name', 'address', 'add_time']


xadmin.site.register(School, SchoolAdmin)
