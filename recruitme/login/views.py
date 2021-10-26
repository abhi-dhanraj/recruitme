from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ApplicantLoginForm, ApplicantSignUpForm
<<<<<<< HEAD
from .models import ApplicantLoggedIn,ApplicantSignedUp
=======
from .models import ApplicantSignedUp, ApplicantLoggedIn
>>>>>>> origin/main

# Create your views here.


def loginSignup(request):
    if request.method == 'POST':
        login_form = ApplicantLoginForm(request.POST)
        signup_form = ApplicantSignUpForm(request.POST)

        if login_form.is_valid():
            print("login form created!")
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
<<<<<<< HEAD
            check = ApplicantSignedUp.objects.raw('SELECT password from ApplicantLoginForm where username = %s'%username)[0]
            print(check.newPassword,password)
            if check==password:
                return redirect('dashboard')
            else:
                return redirect('login-signup-page')  
            # time to save these into mysql database
            # login_form.save()
            return redirect('dashboard')  # should redirect to dashboard
=======
            # time to save these into mysql database
            # form.save()

            # select 1 as id acts as  primary key.
            # query = "select 1 as id,exists(select * from login_applicantsignedup WHERE username='" + \
            #     username+"' and newPassword='"+password+"') as isPresent;"
            query = "select 1 as id, exists(select * from login_applicantloggedin WHERE username='" + \
                username+"' and password='"+password+"') as isPresent;"

            print(query)
            for user in ApplicantSignedUp.objects.raw(query):
                if user.isPresent:
                    print("USER IS PRESENT")
                    # should redirect to dashboard
                    return redirect('dashboard')
                else:
                    print("USER IS NOT PRESENT")
                    # should redirect to login page
                    return redirect('login-signup-page')

>>>>>>> origin/main
        elif signup_form.is_valid():
            print("Signup form Created!")
            username = signup_form.cleaned_data['username']
            emailID = signup_form.cleaned_data['emailID']
            newPassword = signup_form.cleaned_data['newPassword']
            print(username)
            print(emailID)
            print(newPassword)
            # time to save these into mysql database
            signup_form.save()
<<<<<<< HEAD
=======
            ApplicantLoggedIn.objects.create(
                username=username, password=newPassword)
>>>>>>> origin/main
            return redirect('profile')  # should redirect to profile

        else:
            print(login_form._errors)
            print(login_form.clean)
            print("Form is invalid")
    else:
        login_form = ApplicantLoginForm()
        signup_form = ApplicantSignUpForm()

    context = {'login_form': login_form, 'signup_form': signup_form}
    return render(request, 'login/signupLogin.html', context)


