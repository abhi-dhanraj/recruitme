from django.shortcuts import render
from django.http import HttpResponse


def dashboardPage(request):
    print(request.session['username'])
    return render(request, 'recruitme/dashboardPage.html')


def jobsPage(request):
    return render(request, 'recruitme/jobsPage.html')


def jobDetailsPage(request):
    return render(request, 'recruitme/jobDetailsPage.html')


def applicationFormPage(request):
    return render(request, 'recruitme/applicationForm.html')
