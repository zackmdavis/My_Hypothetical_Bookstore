from django.http import HttpResponse
from django.shortcuts import redirect, render_to_response
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.template import RequestContext
import datetime

def home(request):
    current_date = datetime.datetime.now()
    return render_to_response('home.html', locals())

def signup(request):
    pass

def login(request):
    if request.method == 'GET':
        return render_to_response('login.html', RequestContext(request, locals()))
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                messages.success(request, "You've logged in!")
                return redirect('root')
            else:
                messages.error(request, "That account isn't active!")
                return redirect('root')
        else:
            messages.error(request, "Invalid username or password!")
            return redirect('login')

def logout(request):
    pass
