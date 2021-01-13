from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from home.models import Student


def show_all(request):


    students = Student.objects.all()

    return render(
        request = request,
        template_name = 'index.html',
        context = {
            'students' : students,
        }
    )


