from django.conf.urls import url
from .views import *

urlpatterns = [
    url('all/', all),
    url('all_not/', all_not),
    url('all_done/', all_done),
    url('create/', create),
    url('deliver/', deliver),
]
