from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'PasswordGenerator/index.html',{'title': 'Главная страница'})

def generator(request):
    return render(request, 'PasswordGenerator/generator.html',{'title': 'Генератор паролей'})