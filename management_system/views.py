
from django.shortcuts import render
from .models import Student, Course

def home(request):
    return render(request, 'management_system/index.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'management_system/student_list.html', {'students': students})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'management_system/course_list.html', {'courses': courses})
