from django.shortcuts import render
from django.contrib.auth import authenticate, login
# Create your views here.


def login_view(request):
    username = ""
    password = ""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        message = 'Successfully logged in'
    else:
        message = 'Failed to login'
    context = {
        'message': message,
    }
    return render(request, 'user/login.html', context)
