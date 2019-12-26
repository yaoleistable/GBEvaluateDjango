import csv

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from index.models import Standard


# views.py的index函数


# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GBEvaluate.settings')
# django.setup()


# Create your views here.
# index的views.py


def index(request):
    # return HttpResponse("你好，Django !")
    return render(request, 'index.html', context={'title': '首页'}, status=500)
    # return render(request, 'index.html')


def standard(request):
    name_note_list = Standard.objects.values('name', 'note')
    # 相当于数据库查询语句，select name,note from index_standard;
    # context = {'title': '首页', 'name_note_list': name_note_list}
    title = '首页'
    # return render(request, 'standard.html', context=context, status=200)
    # 使用locals()函数，即可把定义的变量传输给模板，模板变量需和这里定义的变量名一致
    return render(request, 'standard.html', context=locals(), status=200)


# 4.4节，通用视图的理解
class StandardList(ListView):
    context_object_name = 'name_note_list'
    template_name = 'standard_view.html'
    queryset = Standard.objects.values('name').distinct()  # 结果查询后去重,结果返给context_object_name

    # 重写 get_queryset()方法，对模型进行数据筛选
    # def get_queryset(self):
    #     name_note_list = Standard.objects.values('name').distinct()
    #     return name_note_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(StandardList, self).get_context_data(**kwargs)
        context['name_note_list'] = Standard.objects.values('name', 'note', 'std_year')
        return context


# def login(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         # return  redirect('http://107.0.0.1:8000/') # 绝对路径
#         return redirect('/')  # 相对路径，代表首页地址
#     else:
#         if request.GET.get('name'):
#             name = request.GET.get('name')
#         else:
#             name = 'Everyone'
#         return HttpResponse('用户名：' + name)
def login(request):
    return render(request, 'login.html')


# views.py的myDate函数
def myDate(request, year, month, day):
    return HttpResponse(str(year) + '/' + str(month) + '/' + str(day))


# views.py的myYear函数
def myYear(request, year):
    return render(request, 'myYear.html')


def myYear_dict(request, year, month):
    return render(request, 'myYear_dict.html', {'month': month})


def download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="camile.csv"'
    writer = csv.writer(response)
    writer.writerow(['first row', 'a', 'b', 'c'])
    return response
