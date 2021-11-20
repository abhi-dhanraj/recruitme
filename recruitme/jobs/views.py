from django.shortcuts import render
from .models import jobs
# Create your views here.

def jobsPage(request):
    query = "select * from jobs_jobs;"
    Jobs = jobs.objects.raw(query)
    for i in Jobs:
        print(i.title)
    context = {"Jobs":Jobs}
    # print(Jobs)
    return render(request, 'jobs/jobsPage.html',context)


def jobDetailsPage(request):
    return render(request, 'jobs/jobDetailsPage.html')

def dashboardPage(request):
    print(request.session['username'])
    return render(request, 'jobs/dashboardPage.html')

