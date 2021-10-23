from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ApplicantLoginForm


# Create your views here.


def loginSignup(request):
    if request.method == 'POST':
        login_form = ApplicantLoginForm(request.POST)
        print("Login form created!")
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            print(username)
            print(password)
            # time to save these into mysql database
            # form.save()
            return redirect('dashboard')  # should redirect to dashboard
        else:
            print(login_form._errors)
            print(login_form.clean)
            print("Form is invalid")
    else:
        login_form = ApplicantLoginForm()
    return render(request, 'login/signupLogin.html', {'login_form': login_form})


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
