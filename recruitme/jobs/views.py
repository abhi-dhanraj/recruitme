from django.shortcuts import render
from .models import jobs
from applicant.models import applicant,institute
from application.models import rounds,process,application

# Create your views here.

def jobsPage(request):
    if 'username' not in request.session:
        request.session['username'] = None
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
    if request.session['username'] is not None:
        applicant_query = "select id from applicant_applicant where username = '"+str(request.session['username'])+"';"
        user = applicant.objects.raw(applicant_query)[0]
        application_query = "select * from application_application where applicant_id_id = "+ str(user.id)+";"
        user_applications = application.objects.raw(application_query)
        total_applied = len(user_applications)
        total_selected = 0
        total_applications = []
        for i in user_applications:
            user_process_query = "select * from application_process where id = " + str(i.process_id_id)+";"
            user_process = process.objects.raw(user_process_query)[0]
            print(user_process.id)
            if user_process.status == 1:
                total_selected+=1
            user_job_query = "select * from jobs_jobs where id = "+str(i.job_id_id)+";"
            user_job = jobs.objects.raw(user_job_query)[0]
            user_round_query = "select * from application_rounds where id = "+str(user_process.round_id_id)+ ";"
            user_round = rounds.objects.raw(user_round_query)[0]
            total_applications.append([i,user_job,user_process,user_round])

            # print(user_process_query,user_job_query,user_round_query)
            context = {'total_applied':total_applied,'total_selected':total_selected,'applications':total_applications}
        pass
    else:
        context = {}
    return render(request, 'jobs/dashboardPage.html',context)

