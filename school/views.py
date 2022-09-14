from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    info = Student.objects.all()
    context = {'info': info}

    return render(request, template, context)
