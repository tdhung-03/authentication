from django.shortcuts import render
from .models import *
# Create your views here.


def view_task(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request, 'task/view_task.html', context)
