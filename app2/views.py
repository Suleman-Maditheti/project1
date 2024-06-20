from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wish1(request):
    return HttpResponse('Hello,Good Morning')
def wish2(request):
    return HttpResponse('Hi,Good Afternoon')
