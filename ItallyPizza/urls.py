"""ItallyPizza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.shortcuts import HttpResponse
from Admins.models import User
from django.conf.urls import url
from json import loads, dumps


def auth(name, password):
    ret = 2
    u = None
    try:
        u = User.objects.get(['name', name])
        ret -= 1
        if u.password == password:
            ret -= 1
    except Exception:
        pass
    return HttpResponse(ret)


def auth_route(request):
    dic = loads(request.body.decode('UTF-8'))
    return auth(name=dic['name'], password=dic['password'])


def create(request):
    dic = loads(request.body.decode('UTF-8'))
    User.objects.create(
        name=dic['name'],
        password=dic['password'],
        isAdmin=dic['isAdmin']
    ).save()
    return HttpResponse(0)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ing/', include('Ingredients.urls')),
    path('des/', include('Deserts.urls')),
    path('meal/', include('Meals.urls')),
    path('drink/', include('Drinks.urls')),
    path('orders/', include('Orders.urls')),
    url('create/', create),
    url('auth/', auth_route),
]
