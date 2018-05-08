from django.shortcuts import render, render_to_response, redirect
from django.http.response import HttpResponse
from app01.models import Asset
# Create your views here.


def add(request, name):
    obj = Asset(host_name=name)
    obj.save()
    return HttpResponse('ok')


def delete(request, id):
    Asset.objects.get(id=id).delete()
    return HttpResponse('delete ok')


def update(request, id, name):
    Asset.objects.filter(id__gt=id).update(host_name=name)
    return HttpResponse('update ok')


def select(request, id):
    obj_list = Asset.objects.filter(id__gt=id).values('id', 'host_name')
    print(obj_list)
    for i in obj_list:
        print(i)
    return HttpResponse(obj_list)


