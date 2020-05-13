from django.shortcuts import render
from django.http import HttpResponse


def my_django(request):
    return HttpResponse('<h1>Hey! I am using Django</h1>')
