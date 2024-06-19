from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def telugu(request):
    return HttpResponse('<h1>Hello,This is telugu Movie</h1>')
def hindi(request):
    return HttpResponse('<h1><marquee>Hello,This is Hindi Film</marquee></h1>')
