from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
from .forms import ApplicantLoginForm, ApplicantSignUpForm
from .models import ApplicantSignedUp, ApplicantLoggedIn
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


def loginSignup(request):
    if request.method == 'POST':
        login_form = ApplicantLoginForm(request.POST)
        signup_form = ApplicantSignUpForm(request.POST)
        if login_form.is_valid():
            print("login form created!")
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            query = "select 1 as id, exists(select * from login_applicantloggedin WHERE username='" + \
                username+"' and password='"+password+"') as isPresent;"

            print(query,request)
            for user in ApplicantSignedUp.objects.raw(query):
                if user.isPresent:
                    print("USER IS PRESENT")
                    # should redirect to dashboard
                    request.session["username"] = username
                    USER = authenticate(username=username, password=password)
                    if USER is not None:
                        login(request,user)
                    return redirect('dashboard')
                else:
                    print("USER IS NOT PRESENT")
                    # should redirect to login page
                    return redirect('login-signup-page')
        elif signup_form.is_valid():
            print("Signup form Created!")
            username = signup_form.cleaned_data['username']
            emailID = signup_form.cleaned_data['emailID']
            newPassword = signup_form.cleaned_data['newPassword']
            USER = User.objects.create_user(username,emailID,newPassword)
            print(username)
            print(emailID)
            print(newPassword)
            query = "select 1 as id, exists(select * from login_applicantsignedup WHERE username='" + \
                username+"' or emailID='"+emailID+"') as isPresent;"
            print(query)
            for user in ApplicantSignedUp.objects.raw(query):
                if user.isPresent:
                    print("USER IS PRESENT")
                    # should redirect to dashboard
                    return redirect('login-signup-page')
                    
                else:
                    print("USER IS NOT PRESENT")
                    # should redirect to login page
                    # time to save these into mysql database
                    signup_form.save()
                    USER.save()
                    USER = authenticate(request, username=username, password=newPassword)
                    if USER is not None:
                        login(request,USER)
                    ApplicantLoggedIn.objects.create(
                        username=username, password=newPassword)
                    request.session["username"] = username
                    return redirect('profile-page')  # should redirect to profile

        else:
            print(login_form._errors)
            print(login_form.clean)
            print("Form is invalid")
    else:
        login_form = ApplicantLoginForm()
        signup_form = ApplicantSignUpForm()

    context = {'login_form': login_form, 'signup_form': signup_form}
    return render(request, 'login/signupLogin.html', context)


def loginPage(request):
    form = ApplicantLoginForm()
    if request.method == 'POST':
        form = ApplicantLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # form.save()
            USER = authenticate(request, username=username, password=password)
            if USER is not None:
                login(request,USER)
            print(username)
            print(password)
            request.session["username"] = username

            # time to save these into mysql database
            return redirect('dashboard')  # should redirect to dashboard

    return render(request, 'login/login.html', {'form': form})

def Logout(request):
    logout(request)
    request.session['username'] = None
    return redirect('jobs')