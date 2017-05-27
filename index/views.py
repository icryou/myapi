# coding:utf-8
from django.shortcuts import render
from .models import MicroService, CreateTestApi
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

# Create your views here.


# def test_api_manage(request):
#         # api列表
#         api_list = CreateTestApi.objects.all()
#         return render(request, "index.html", {"api_list": api_list})

# def service_manage(request):
#     # 微服务列表
#     service_list = MicroService.objects.all()
#     paginator = Paginator(service_list, 2)
#     page = request.GET.get('page')
#     try:
#         contacts = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer, deliver first page.
#         contacts = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range (e.g. 9999), deliver last page of results.
#         contacts = paginator.page(paginator.num_pages)
#     return render(request, "index.html", {"services": contacts})


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


def editor_delete(request):
    # 删除勾选的接口信息
    checkList = request.POST.getlist('checkItem')
    btnVal = request.POST.get('btnDelete')
    if checkList and btnVal == 'btnDelete':
        for newId in checkList:
            CreateTestApi.objects.filter(id=newId).delete()
            messages.success(request, r"Selected for Editor" + " is deleted.")
            checkList.remove(newId)
    elif btnVal == 'btnDelete':
        messages.error(request, r"Deleted for Editor" + " is not Selected.")
    else:
        pass