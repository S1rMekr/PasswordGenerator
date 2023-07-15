from django.shortcuts import render
from django.http import HttpResponseNotFound
from .generator import *

# Create your views here.
menu = [{'title': 'Генератор паролей', 'url': 'generator'},
        {'title': 'Новая фича 1', 'url': 'feature1'},
        {'title': 'Новая фича 2', 'url': 'feature2'}]


def index(request):
    return render(request, 'PasswordGenerator/index.html', {'title': 'Главная страница', 'menu': menu})


def generator(request):
    password = password_generator()
    return render(request, 'PasswordGenerator/generator.html', {'menu': menu, 'password': password, 'title': 'Генератор паролей'})


def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Страница не найдена</h1>')
