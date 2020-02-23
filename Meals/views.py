from django.shortcuts import HttpResponse
from .models import *
from django.core.serializers import serialize
from json import loads
from base64 import b64decode


# Create your views here.
def createType(request):
    map = loads(request.body.decode('UTF-8'))
    try:
        Types.objects.create(name=map['name'], image=b64decode(map['img'])).save()
        print('created')
        return HttpResponse('0')
    except Exception:
        print('rejected')
        return HttpResponse('1')


def createMeal(request):
    map = loads(request.body.decode('UTF-8'))
    try:
        Meal.objects.create(
            name=map['name'],
            image=b64decode(map['img']),
            cost=map['cost'],
            type=Types.objects.get(pk=map['type']),
            ingredient=map['ingredient'],
            additional_meals=map['additional_meals'],
            additional_drinks=map['additional_drinks'],
            additional_deserts=map['additional_deserts'],

        ).save()
        return HttpResponse('0')
    except Exception as e:
        return HttpResponse('1')


def allTypes(request):
    return HttpResponse(serialize('json', Types.objects.all()))


def by_type(request):
    pk = request.GET.get('id')
    ret = Meal.objects.filter(type=Types.objects.get(pk=pk))
    return HttpResponse(serialize('json', ret))


def del_type(request):
    pk = request.GET.get('id')
    Types.objects.get(pk=pk).delete()
    return HttpResponse('0')


def allMeals(request):
    return HttpResponse(serialize('json', Meal.objects.all()))


def del_meal(request):
    pk = request.GET.get('id')
    Meal.objects.get(pk=pk).delete()
    return HttpResponse('0')


def get_meal(request):
    pk = request.GET.get('id')
    m = Meal.objects.get(pk=pk)
    return HttpResponse(serialize('json', [m]))
