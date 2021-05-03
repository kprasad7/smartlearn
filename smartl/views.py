from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test


def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')  
    return render(request,'student/student-main.html')


def is_teacher(user):
    return user.groups.filter(name='TEACHER').exists()

def is_student(user):
    return user.groups.filter(name='STUDENT').exists()

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def afterlogin_view(request):
    if is_student(request.user):      
        return redirect('s/student-main')

def main(request):
    return render(request , "base.html" )
def logout(request):
    return render(request , "logout.html" )    