#from django.db import models

# Create your models here.

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    department = models.CharField(max_length=50)
    year_of_study = models.IntegerField()
    academic_performance = models.FloatField()

    def __str__(self):
        return self.name


class Company(models.Model):
    company_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=50)
    job_role = models.CharField(max_length=100)
    placement_date = models.DateField()

    def __str__(self):
        return self.company_name


class Placement(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Placed', 'Placed'),
        ('Rejected', 'Rejected')
    ])

    def __str__(self):
        return f"{self.student.name} - {self.company.company_name}"

