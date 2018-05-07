#!/usr/bin/python35
# -*- coding: utf-8 -*-
# author: WangDaWei
from django.http.response import HttpResponse


def func1(request, content):
    print(content)
    m = content.split('/')[0]
    f = content.split('/')[1]
    obj = __import__(m + '.views', fromlist=True)
    if hasattr(obj, f):
        result = getattr(obj, f)(request)
        return result
    else:
        return HttpResponse("404")


