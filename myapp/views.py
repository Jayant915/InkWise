
from django.shortcuts import render
from django.http import HttpResponse

#def home(request):
 #   return HttpResponse("Hello, Django!")

#def home(request):
   # return render(request, 'myapp/index.html')

def index(request):
    return render(request, 'index.html')

def pricing(request):
    return render(request, 'pricing.html')

def team(request):
    return render(request, 'team.html')


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')
