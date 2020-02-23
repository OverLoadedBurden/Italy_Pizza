from django.shortcuts import HttpResponse
from .models import Drink
from django.core.serializers import serialize
from json import loads
from base64 import b64decode


# Create your views here.
def create(request):
    map = loads(request.body.decode('UTF-8'))
    try:
        Drink.objects.create(name=map['name'], cost=map['cost'], image=b64decode(map['img'])).save()
        return HttpResponse('0')
    except Exception:
        return HttpResponse('1')


def all(request):
    return HttpResponse(serialize('json', Drink.objects.all()))


def delete(request):
    pk = request.GET.get('id')
    Drink.objects.get(pk=pk).delete()
    return HttpResponse('0')


def get(request):
    pk = request.GET.get('id')
    d = Drink.objects.get(pk=pk)
    return HttpResponse(serialize('json', [d]))
