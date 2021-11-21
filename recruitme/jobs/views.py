from django.db.models import query
from django.shortcuts import render
from .models import jobs
# Create your views here.


def jobsPage(request):
    query = "select * from jobs_jobs;"
    Jobs = jobs.objects.raw(query)
    for i in Jobs:
        print(i.title)
    context = {"Jobs": Jobs}
    # print(Jobs)
    return render(request, 'jobs/jobsPage.html', context)


def jobDetailsPage(request, job_id):

    query = "select * from jobs_jobs where job_id=" + str(job_id) + " ;"
    print(query)
    Job = jobs.objects.raw(query)[0]
    print(Job.title)
    context = {"Job": Job}
    return render(request, 'jobs/jobDetailsPage.html', context)


def dashboardPage(request):
    print(request.session['username'])
    return render(request, 'jobs/dashboardPage.html')


def applicationFormPage(request, job_id):
    print(job_id)
    query = "select * from jobs_jobs where job_id=" + str(job_id) + " ;"
    Job = jobs.objects.raw(query)[0]
    context = {"JobTitle": Job.title}
    return render(request, 'recruitme/applicationForm.html', context)
