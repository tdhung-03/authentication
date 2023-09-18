from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.


@login_required(login_url='login')
def view_task(request):
    tasks = Task.objects.filter(user=request.user)
    context = {
        'tasks': tasks,
    }
    return render(request, 'task/view_task.html', context)


@login_required(login_url='login')
def create_task(request):
    user = request.user
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = user
            task.save()
    context = {
        'form': form
    }
    return render(request, 'task/create_task.html', context)
