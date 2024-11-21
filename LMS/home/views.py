from django.shortcuts import render,redirect
from home.models import *
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        user = User.objects.filter(username=username)
        if user.exists:
            messages.warning(request, "Username already taken.")
        user = User.objects.create(first_name=first_name,last_name=last_name,username=username,email=email)
        user.set_password(password)
        user.save()
        return redirect('login_page')
    return render(request,'register.html')



def login_page(request):
    if request.method == 'POST':
        data = request.POST
        username= data.get('username')
        password = data.get('password')

        if not User.objects.filter(username=username).exists:
            messages.error(request, "Invalid username.")
            return redirect('login_page')
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request,'Invalid username or password.')
        else:
            login(request,user)
            return redirect('home')
    return render(request,'login.html')

@login_required(login_url='login_page')
def home(request):
    if request.method == 'POST':
        data = request.POST
        full_name = data.get('full_name')
        age = data.get('age')
        email = data.get('email')
        address = data.get('address')
        department_id = data.get('deprt')
        department_obj = department.objects.get(id=department_id)
        # student_ids = data.get('student_id')
        # student_obj = student_id.objects.get(id=student_ids)
        student = Student.objects.create(full_name=full_name,age=age,email=email,address=address,d=department_obj)
        student.save()
        messages.success(request, "Details added successfully.")
    deprt = department.objects.all()
    return render(request, 'index.html',context={'deprt':deprt})



def logout_page(request):
    logout(request)
    return redirect('login_page')



def display(request):
    studnt = Student.objects.all()
    return render(request,'display.html', context={'studnt' : studnt})