from django.urls import path,re_path
from .views import *

urlpatterns = [
    path('index/',index),
    path('addUser/',addUser),
    path('getData/',getData),
    path('updateUser/',updateUser),
    path('deleteUser/',deleteUser),
    path('doubleLine/',doubleLine),
    path('OneToManyAdd/',OneToManyAdd),
    path('OneToManyGet/',OneToManyGet),
    path('OneToManyUpdate/',OneToManyUpdate),
    path('OneToManyDelete/',OneToManyDelete),
    path('ManyAdd/',ManyAdd),
    path('ManyGet/',ManyGet),
    path('ManyUpdate/',ManyUpdate),
    path('ManyDelete/',ManyDelete),
    path('juhe/',juhe),
]