from django.urls import path
from . import views

urlpatterns = [
    # path('todos/', views.Todo_Json),
    path('generics/', views.TodoGenericApiView.as_view()),
    path('generics/<pk>', views.TodoGenericsDetailView.as_view())

]