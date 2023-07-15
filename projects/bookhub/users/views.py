from typing import Any
from django import http
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views import View
import json


def hello(request):

    print(request.method)
    return HttpResponse("hello")


def user(request, name, phone):

    return HttpResponse(f"Hello, {name}. {phone}")

def fullname(request, first_name, last_name):
    return HttpResponse(f"{first_name} {last_name}")


class ClassBasedView(View):

    def get(self, request):
        name = request.GET.get("name", "Noname")
        print("name query parameter", name)
        return HttpResponse("hello from GET")
    
    def post(self, request):
        data = json.loads(request.body)
        name = data.get('name')
        print("name post parameter", name)
        return HttpResponse("hello from POST")
    
    def patch(self, request):
        return HttpResponse("Пользователь изменен")
    
    def delete(self, request):
        return HttpResponse("Пользователь удален")
    

class DispatchView(View):
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        
        if request.method == 'GET':
            return self.get_username(request, *args, **kwargs)
    
    def get_username(self, request, *args, **kwargs):
        return HttpResponse("username")