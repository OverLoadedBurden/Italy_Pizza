from django.conf.urls import url
from .views import *

urlpatterns = [
    url('allTypes/', allTypes),
    url('by_type/', by_type),
    url('get/', get_meal),
    url('del_type', del_type),
    url('del_meal', del_meal),
    url('create_type/', createType),
    url('allMeals/', allMeals),
    url('create_meal/', createMeal),
]
