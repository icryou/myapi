# coding:utf-8
from django.shortcuts import render
from .models import MicroService, CreateTestApi
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse


# Create your views here.


def test_api_manage(request):
    # 接口列表
    api_list = CreateTestApi.objects.all()
    paginator = Paginator(api_list, 10)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, "index.html", {"api_list": contacts})


def get_table_data(request):
    # 接收提交的表格数据
    return HttpResponse(request.GET)