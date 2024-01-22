from  django.urls import  path
from  . import  views

urlpatterns = [
    path('', views.Todo_Json)
]