from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    # check to see if logging in
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']
        # authenticate
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('home')
    else:
        return render(request, 'home.html', {})


def logout_user(request):
    pass