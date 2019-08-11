from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def contact(*args, **kwargs):
    return HttpResponse('<h1>This is contact page</h1>')