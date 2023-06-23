import json

from django.views import View
from django.shortcuts import render
from django.http import HttpResponse

class ClassBasedView(View):

    def get(self, request):
        message = f'Hello, from GET method!'
        return HttpResponse(message)

    def post(self, request):
        data = json.loads(request.body)
        name = data.get('name')
        message = f'Hello {name}, from POST method!'
        return HttpResponse(message)
