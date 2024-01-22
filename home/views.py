from django.shortcuts import render
from rest_framework.request import Request
from todo.models import Todo
from rest_framework.response import Response
from django.http import response, request, HttpRequest, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET'])
def Todo_Json(request:Request):
    todos = list(Todo.objects.order_by('priority').all().values('title', 'is_done'))
    return Response({'todos':todos}, status.HTTP_200_OK)
