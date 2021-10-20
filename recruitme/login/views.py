from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ApplicantLoginForm

# Create your views here.


def loginSignup(request):
    return render(request, 'login/signupLogin.html')


def loginPage(request):
    form = ApplicantLoginForm()
    if request.method == 'POST':
        form = ApplicantLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # form.save()

            print(username)
            print(password)
            # time to save these into mysql database
            return redirect('dashboard')  # should redirect to dashboard

    return render(request, 'login/login.html', {'form': form})
