from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def loginPage(request):
    return render(request, 'login/login.html')


def home(request):
    return HttpResponse("This is Home page!!!!")
