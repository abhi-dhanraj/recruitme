from django.shortcuts import render
from django.http import HttpResponse
from .forms import ApplicantLoginForm

# Create your views here.


def home(request):
    return HttpResponse("This is Home page!!!!")


def loginPage(request):
    form = ApplicantLoginForm()
    if request.method == 'POST':
        form = ApplicantLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username)
            print(password)
            # time to save these into mysql database

    return render(request, 'login/login.html', {'form': form})
