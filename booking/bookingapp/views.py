from django.shortcuts import render, HttpResponse
import random

# Create your views here.

def index(request):
    
    return render(request, "index.html")

def rand(request):
    rnumber = random.randint(1000,9999)
    return HttpResponse(rnumber)
