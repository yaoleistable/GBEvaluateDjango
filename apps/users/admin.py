from django.contrib import admin

from .models import UserProfile


# Register your models here.

# 方法一：注册models
# admin.site.rigister(UserProfile)


# 方法二：继承实现，常用
class UserProfileAdmin(admin.ModelAdmin):
    # pass
    # 显示的字段
    list_display = ['username', 'address', 'mobile']


admin.site.register(UserProfile, UserProfileAdmin)
