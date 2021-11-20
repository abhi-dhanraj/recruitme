from django.shortcuts import render
from django.http import HttpResponse


def applicationFormPage(request):
    return render(request, 'recruitme/applicationForm.html')
