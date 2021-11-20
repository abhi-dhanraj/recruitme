from django.shortcuts import render
from .models import jobs
# Create your views here.

def jobsPage(request):
    query = "select * from jobs_jobs;"
    Jobs = jobs.objects.raw(query)
    context = {"Jobs":Jobs}
    return render(request, 'jobs/jobsPage.html',context)


def jobDetailsPage(request,job_id):
    print(job_id)
    query = "select * from jobs_jobs where job_id = "+str(job_id)+";"
    Job = jobs.objects.raw(query)[0]
    context = {"Job":Job}
    return render(request, 'jobs/jobDetailsPage.html',context)

def dashboardPage(request):
    print(request.session['username'])
    return render(request, 'jobs/dashboardPage.html')

