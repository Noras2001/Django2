from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main/index.html')
    #return HttpResponse('<h1>Mi primer projecto Django</h1>')

def new(request):
    return render(request, 'main/new.html')
    #return HttpResponse('<h1>Otra página</h1>')

def new3(request):
    return render(request, 'main/new3.html')

def new4(request):
    return render(request, 'main/new4.html')