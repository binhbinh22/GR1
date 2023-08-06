from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'page/home.html')

def contact(request):
    return render(request, 'page/contact.html')

def error(request, exception):
    return render(request, 'page/error.html',status=404)

def model(request):
    return render(request, 'page/model.html')

