from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return HttpResponse("Hello world")
