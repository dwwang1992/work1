"""Django_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from Django_1.common import func1
from app01 import views1
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('add/<str:group_name>/<str:type_name>/', views.add),
    path('select11/', views.select),

    path('add/<str:name>/', views1.add),
    path('delete/<int:id>/', views1.delete),
    path('update/<int:id>/<str:name>/', views1.update),
    path('select/<int:id>/', views1.select),
    re_path('(.*)/', func1),

]

