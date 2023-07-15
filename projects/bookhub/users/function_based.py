from django.shortcuts import render
from django.http import HttpResponse

def function_based_view(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('name', "Not exist")
        message = f'Hello {name}, from POST method!'
        return HttpResponse(message)
    
    message = f'Hello, from GET method!'
    return HttpResponse(message)