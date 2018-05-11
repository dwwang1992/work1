from django.shortcuts import render, render_to_response, redirect
from django.http.response import HttpResponse
# Create your views here.
from app01.models import User


def login(request):
    return render_to_response("app01/login.html")


def index(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user_obj = User.objects.filter(username=username, password=password).values()
    if user_obj.count() == 1:
        address = user_obj[0]['address']
        phone = user_obj[0]['phone']
        create_time = user_obj[0]['create_time']
        update_time = user_obj[0]['update_time']
        info = user_obj[0]['info']
        ret = dict()
        ret['username'] = username
        ret['password'] = password
        ret['address'] = address
        ret['phone'] = phone
        ret['create_time'] = create_time
        ret['update_time'] = update_time
        ret['info'] = info
        return render_to_response("app01/index.html", ret)
    else:
        return redirect("/login/")


def first(request):
    return render_to_response("app01/first.html")

