from django.shortcuts import render, redirect
from django.http import HttpResponse

from home.forms import StudentForm
from home.models import Student


def show_all(request):


    students = Student.objects.all()

    student_form = StudentForm()
    context = {
            'students' : students,
            'form' : student_form,
        }

    return render(request, 'index.html',
        context = context)


def add_student_with_form(request):

    if request.method == 'GET':

        student_form = StudentForm()
        context = {
            'student_form' : student_form,
        }
        return render(request, 'student_form.html', context = context)

    elif request.method == 'POST':

        student_form = StudentForm(request.POST)

        if student_form.is_valid():
            student_form.save()

        return redirect('http://localhost:8000/students/')


