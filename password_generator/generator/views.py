from django.shortcuts import render
from django.http import HttpResponse                           # добавляем строку
import random

# Create your views here.

def home(request):                                             # добавляем строку
    #return HttpResponse('Привет, Вы запустили views.home')     # добавляем строку вариант1
    #return render(request, 'generator/home.html')              # внесли изменение вариант2
    #return render(request, 'generator/home.html', {'password':'acsoJ!2@3JLKJbj9097%^90'})              # внесли изменение вариант3
    return render(request, 'generator/home.html')              # внесли изменение вариант4

def password(request):                                             # добавляем строку
    #return HttpResponse('Привет, Вы запустили views.func')     # добавляем строку
    #return render(request, 'generator/password.html')              # внесли изменение вариант4
    #thepassword = 'testing'                      # вводим переменную, которая будет отображать password
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('numbers'):
        characters.extend('0123456789')
    if request.GET.get('special'):
        characters.extend('!@#$%^&*')
    #length = 10
    length = int(request.GET.get('length'))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password':thepassword})              # внесли изменение вариант5

def page1(request):
    return render(request, 'generator/page1.html')
