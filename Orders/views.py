from django.shortcuts import HttpResponse
from .models import *
from django.core.serializers import serialize
from json import loads
from base64 import b64decode


# Create your views here.
def create(request):
    map = loads(request.body.decode('UTF-8'))
    try:
        Order.objects.create(
            name=map['name'],
            location=map['location'],
            drinks=map['drinks'],
            meals=map['meals'],
            deserts=map['deserts'],
            phone=map['phone'],
            total=map['cost'],
        ).save()
        return HttpResponse('0')
    except Exception as e:
        return HttpResponse('1')


def all(request):
    return HttpResponse(serialize('json', Order.objects.all()))


def deliver(request):
    id = request.GET.get('id')
    Order.objects.get(id=id).deliver()
    return HttpResponse('0')


def all_not(request):
    return HttpResponse(serialize('json', Order.objects.filter(done=False)))


def all_done(request):
    return HttpResponse(serialize('json', Order.objects.filter(done=True)))
