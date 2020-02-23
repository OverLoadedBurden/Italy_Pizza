from django.shortcuts import HttpResponse
from .models import Ingredient
from django.core.serializers import serialize
from json import loads
from base64 import b64decode


# Create your views here.
def create(request):
    map = loads(request.body.decode('UTF-8'))
    try:
        Ingredient.objects.create(name=map['name'], image=b64decode(map['img'])).save()
        print('created')
        return HttpResponse('0')
    except Exception:
        print('rejected')
        return HttpResponse('1')


def all(request):
    return HttpResponse(serialize('json', Ingredient.objects.all()))


def delete(request):
    pk = request.GET.get('id')
    Ingredient.objects.get(pk=pk).delete()
    return HttpResponse('0')


def get(request):
    pk = request.GET.get('id')
    i = Ingredient.objects.get(pk=pk)
    return HttpResponse(serialize('json', [i]))
