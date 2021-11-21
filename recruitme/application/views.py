from django.shortcuts import redirect, render
import datetime
from applicant.models import applicant, institute
from .forms import Application
from jobs.models import jobs
from .models import rounds, process, application
# Create your views here.


def applicationFormPage(request, job_id):
    appform = Application()
    if request.method == "POST":
        appform = Application(request.POST)
        print(appform.is_valid())
        if appform.is_valid():
            print("YESSS")
            round = rounds.objects.create(
                aptitude=0, interview=0, professional_fitment=0, hr=0, stage=0, total_points=0)
            round.save()
            Process = process.objects.create(status=False, round_id=round)
            Process.save()
            institute_id = appform.cleaned_data['institute_id']
            Degree = appform.cleaned_data['degree']
            Year = appform.cleaned_data['graduation_year']
            Cgpa = appform.cleaned_data['cgpa']
            Experience = appform.cleaned_data['experience']
            Ans = appform.cleaned_data['ans']
            print(institute_id, Ans, request.session['username'])

            applicant_query = "select id from applicant_applicant where username = '" + \
                str(request.session['username'])+"';"
            institute_query = "select * from applicant_institute where institute_id = '" + \
                str(institute_id)+"';"
            job_query = "select * from jobs_jobs where job_id = '" + \
                str(job_id)+"';"
            user_applicant = applicant.objects.raw(applicant_query)[0]
            user_institute = institute.objects.raw(institute_query)[0]
            user_job = jobs.objects.raw(job_query)[0]
            application.objects.create(applicant_id=user_applicant, process_id=Process, job_id=user_job, cgpa=Cgpa, experience=Experience, graduation_year=Year,
                                       ans=Ans, degree=Degree, institute_id=user_institute, date_of_application=datetime.datetime.now().strftime("%Y-%m-%d"))
            return redirect('dashboard')
    query = "select * from jobs_jobs where job_id=" + str(job_id) + " ;"
    Job = jobs.objects.raw(query)[0]
    context = {"JobTitle": Job.title, "appform": appform}
    return render(request, 'application/applicationForm.html', context)


'''
insert into applicant_institute(institute_id,name,tnp_contact,students_applied) values
('PICT','Pune Institute of Computer Technology',7593726489,0),
('COEP','College of Engineering Pune',9472947362,0),
('AIT','Army Institute of Computer Technology',8278493134,0),
('VIT','Vishwakarma Institute of Technology',8950385234,0);
'''
