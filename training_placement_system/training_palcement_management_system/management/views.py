#from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Student, Company, Placement

def index(request):
    return render(request, 'index.html')

def students(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        department = request.POST['department']
        year_of_study = request.POST['year_of_study']
        academic_performance = request.POST['academic_performance']
        Student.objects.create(
            name=name,
            email=email,
            phone_number=phone_number,
            department=department,
            year_of_study=year_of_study,
            academic_performance=academic_performance,
        )
        return redirect('student')
    students = Student.objects.all()
    return render(request, 'student.html', {'student': students})

def companies(request):
    if request.method == 'POST':
        company_name = request.POST['company_name']
        industry = request.POST['industry']
        job_role = request.POST['job_role']
        placement_date = request.POST['placement_date']
        Company.objects.create(
            company_name=company_name,
            industry=industry,
            job_role=job_role,
            placement_date=placement_date,
        )
        return redirect('companies')
    companies = Company.objects.all()
    return render(request, 'companies.html', {'companies': companies})

def placement(request):
    if request.method == 'POST':
        student_id = request.POST['student_id']
        company_id = request.POST['company_id']
        status = request.POST['status']
        Placement.objects.create(
            student_id=student_id,
            company_id=company_id,
            status=status,
        )
        return redirect('placement')
    
    placements = Placement.objects.select_related('student', 'company').all()
    students = Student.objects.all()
    companies = Company.objects.all()
    return render(request, 'placement.html', {
        'placements': placements,
        'students': students,
        'companies': companies,
    })
