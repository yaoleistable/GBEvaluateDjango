from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class UserProfile(AbstractUser):
    # 自定义用户，继承自系统
    nick_name = models.CharField(max_length=50, verbose_name="昵称", default='', blank=True)
    birday = models.DateField(verbose_name="生日", blank=True, null=True)
    gender = models.CharField(choices=(('male', "男"), ('female', "女")),
                              default='male', verbose_name="性别", max_length=6)
    address = models.CharField(max_length=100, default='', verbose_name="地址", blank=True)
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name="手机")
    # 使用ImageField，需要安装Pillow库
    image = models.ImageField(upload_to='image/%Y/%m', default="image/default.jpg",
                              verbose_name="头像", max_length=100, blank=True)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class School(models.Model):
    """
    学校表
    """
    name = models.CharField(max_length=50, verbose_name='学校名字')
    address = models.CharField(max_length=100, verbose_name='学校地址')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '学校'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
