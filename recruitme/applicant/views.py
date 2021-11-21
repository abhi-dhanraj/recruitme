from django.shortcuts import render
from .forms import Applicant
# Create your views here.


def profilepage(request):
    profile = Applicant()
    if request.method == "POST":
        profile = Applicant(request.POST)
        if profile.is_valid():
            profile.save()
    context = {'profile': profile}
    return render(request, 'applicant/profilePage.html', context)
