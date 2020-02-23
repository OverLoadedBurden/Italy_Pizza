from django.conf.urls import url
from .views import *

urlpatterns = [
    url('all/', all),
    url('create/', create),
    url('del/', delete),
    url('get', get),
]
