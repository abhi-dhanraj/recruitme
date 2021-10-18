from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# def mainPage(request):
#     # return HttpResponse("This is HomePage")
#     return render(request, 'recruitme/main.html')


def dashboardPage(request):
    return render(request, 'recruitme/dashboardPage.html')


def profilePage(request):
    return render(request, 'recruitme/profilePage.html')


def jobsPage(request):
    return render(request, 'recruitme/jobsPage.html')


def jobDetailsPage(request):
    return render(request, 'recruitme/jobDetailsPage.html')
