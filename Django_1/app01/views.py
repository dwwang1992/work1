from django.shortcuts import render, render_to_response, redirect
from django.http.response import HttpResponse
# Create your views here.
from app01.models import UserInfo, UserGroup, UserType


def index(request):
    return HttpResponse("app01_index")


def login(request):
    return render_to_response("app01/user.html", {'name': 'dave'})


def add(request, group_name, type_name, user_name='link', user_password='123456', user_email='dave@126.com'):

    group_obj = UserGroup.objects.get(groupname=group_name)
    type_obj = UserType.objects.get(typename=type_name)
    user_obj = UserInfo.objects.create(username=user_name, password=user_password, email=user_email, type=type_obj)
    # 将用户添加到对应的组中，以下两个方法都可以
    group_obj.userinfo_set.add(user_obj)
    # user_obj.group_relation.add(group_obj)

    return HttpResponse('add ok')


def select(request):

    user_list = UserInfo.objects.filter(type__typename='administrator')

    for item in user_list:
        print(item.username, item.password, item.email)
        print(item.type.id, item.type.typename)

    return HttpResponse('ok')





