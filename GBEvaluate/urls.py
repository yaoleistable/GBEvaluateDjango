"""GBEvaluate URL Configuration

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
# 根目录的urls
from django.contrib import admin  # 导入admin功能模块
from django.urls import path, include
import xadmin

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin站点管理
    path('xadmin/', xadmin.site.urls),  # xadmin站点管理
    path('', include('index.urls'))  # 定义首页地址
]
