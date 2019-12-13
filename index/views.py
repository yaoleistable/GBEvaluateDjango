from django.shortcuts import render

# Create your views here.

# index的views.py

from django.http import HttpResponse


# views.py的index函数
def index(request):
    return HttpResponse("你好，Django !")


# views.py的myDate函数
def myDate(request, year, month, day):
    return HttpResponse(str(year) + '/' + str(month) + '/' + str(day))


# views.py的myYear函数
def myYear(request, year):
    return render(request, 'myYear.html')


def myYear_dict(request, year, month):
    return render(request, 'myYear_dict.html', {'month': month})


