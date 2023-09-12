from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
# Create your views here.


def login_view(request):
    username = ""
    password = ""
    message = ""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("view_task")
    else:
        message = "Failed to login"
    context = {
        'message': message,
    }
    return render(request, 'user/login.html', context)


def logout_view(request):
    logout(request)
    return redirect("view_task")
