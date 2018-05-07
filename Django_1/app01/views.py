from django.shortcuts import render, redirect
from django.http.response import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("app01_index")


def login(request):
    return redirect('/app02/index/')
