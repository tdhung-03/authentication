from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def view_task(request):
    tasks = Task.objects.filter(user=request.user)
    context = {
        'tasks': tasks,
    }
    return render(request, 'task/view_task.html', context)
