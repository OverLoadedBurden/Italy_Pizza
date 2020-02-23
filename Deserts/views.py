from django.shortcuts import HttpResponse
from .models import Desert
from django.core.serializers import serialize
from json import loads, dumps
from base64 import b64decode


# Create your views here.
def create(request):
    map = loads(request.body.decode('UTF-8'))
    try:
        Desert.objects.create(name=map['name'], ingredient=map['ings'], cost=map['cost'],
                              image=b64decode(map['img'])).save()
        return HttpResponse('0')
    except Exception:
        return HttpResponse('1')


def all(request):
    return HttpResponse(serialize('json', Desert.objects.all()))


def get(request):
    return HttpResponse(serialize('json', Desert.objects.all()))


def delete(request):
    pk = request.GET.get('id')
    Desert.objects.get(pk=pk).delete()
    return HttpResponse('0')


def get(request):
    pk = request.GET.get('id')
    d = Desert.objects.get(pk=pk)
    return HttpResponse(serialize('json', [d]))
