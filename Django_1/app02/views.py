from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("app02_index")


def login(request):
    return HttpResponse("app02_login")
