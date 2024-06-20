from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def company1(request):
    return HttpResponse('Product based company:Google')
def company2(request):
    return HttpResponse('Service Based Company:Infosys')