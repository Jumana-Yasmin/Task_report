from .forms import StudentForm
from .models import Student, Course
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect


def student_register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('eligible_courses', student_id=student.id)
    else:
        form = StudentForm()
    return render(request, 'student_register.html', {'form': form})


def eligible_courses(request, student_id):
    student = Student.objects.get(id=student_id)
    eligible_courses = Course.objects.filter(required_education=student.
                                             education)
    return render(request, 'eligible_courses.html',
                  {'student': student, 'courses': eligible_courses})


def home(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())
