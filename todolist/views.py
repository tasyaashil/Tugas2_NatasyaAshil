import datetime
from multiprocessing import context

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render
from todolist.models import Tasktodolist

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from todolist.forms import taskform

# Create your views here.
@login_required(login_url='/todolist/login/')

def show_todolist(request) :
    datatodolist = Tasktodolist.objects.filter(user=request.user)
    context = {
    'list_todolist' : datatodolist,
    'last_login': request.COOKIES['last_login'],
    }
    return render(request, 'todolist.html', context)

def register(request) :
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request) :
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def add_todolist(request):
    form = taskform()
    if request.method == "POST":
        form = taskform(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('todolist:show_todolist')
    context = {'form': form}
    return render(request, 'add_todolist.html', context)

