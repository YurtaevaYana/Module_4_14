from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(requests):
    return HttpResponse('Успешно!') # возвращаем текст "Успешно!" в качестве ответа на странице
