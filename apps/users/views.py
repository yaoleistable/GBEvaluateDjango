from django.shortcuts import render

# Create your views here.
from .models import UserMessage


def getform(request):
    # 读取信息
    # all_messages = UserMessage.objects.all()
    message = None
    all_messages = UserMessage.objects.filter(name='linyan')
    if all_messages:
        message = all_messages[0]
    # for message in all_messages:
    # message.delete()  # 删除数据库内容
    # print(message.message)

    # 写入信息
    # user_message = UserMessage()
    # user_message.name = "姚蕾"
    # user_message.email = "989@11.com"
    # user_message.address = "广州市"
    # user_message.message = "测试信息"
    # user_message.save()
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        address = request.POST.get("address", "")
        message = request.POST.get("message", "")
        user_message = UserMessage()
        user_message.name = name
        user_message.email = email
        user_message.address = address
        user_message.message = message
        user_message.save()

    return render(request, 'form_message.html', {"my_message": message})
