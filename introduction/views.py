from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def intro(request):
    return HttpResponse("<h1>Hello There</h1>")


def achievements(request):
    return HttpResponse("<h1>My Achievements</h1>")
