from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.request import Request
from  rest_framework.response import Response
from .serializers import TodoSerializers
from todo.models import Todo
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
# @api_view(['GET'])
# def Todo_Json(request:Request):
#     todos = Todo.objects.order_by('priority').all()
#     todo_serializer = TodoSerializers(todos, many=True)
#     return Response(todo_serializer.data, status.HTTP_200_OK)


class TodoGenericApiView(generics.ListCreateAPIView):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializers
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class TodoGenericsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializers
