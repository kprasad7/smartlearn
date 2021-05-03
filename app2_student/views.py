from django.shortcuts import render,redirect,reverse
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from . import forms
from . import models
from app2_student.models import Studentt
from app2_student.forms import StudentForm , StudentUserForm
from smartl.views import is_student
from app1_test.models import Course , Questiont,Result
from smartl.views import is_student
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.core.paginator import Paginator
    



def student_signup_view(request):
    userForm=forms.StudentUserForm()
    studentForm=forms.StudentForm()
    mydict={'userForm':userForm,'studentForm':studentForm}
    if request.method=='POST':
        userForm=forms.StudentUserForm(request.POST)
        studentForm=forms.StudentForm(request.POST)
        if userForm.is_valid() and studentForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            student=studentForm.save(commit=False)
            student.user=user
            student.save()
            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
        return HttpResponseRedirect('studentlogin')
    return render(request,'signup.html',context=mydict)

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_main(request):
    return render(request , "student/student-main.html")
@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_exam_view(request):
    
    dict={
        "courses":Course.objects.all(),
        "stud":Studentt.objects.get(user_id=request.user.id)
        
    }
    return render(request,'student/student_exam.html',context=dict)

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_exam_view5(request):
    
    dict={
        "courses":Course.objects.filter(course_name="science"),
        "stud":Studentt.objects.get(user_id=request.user.id)
        
    }
    return render(request,'student/student_exam.html',context=dict)
@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_exam_view4(request):
    
    dict={
        "courses":Course.objects.filter(course_name="maths"),
        "stud":Studentt.objects.get(user_id=request.user.id)
        
    }
    return render(request,'student/student_exam.html',context=dict)
@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_exam_view3(request):
    
    dict={
        "courses":Course.objects.filter(course_name="social"),
        "stud":Studentt.objects.get(user_id=request.user.id)
        
    }
    return render(request,'student/student_exam.html',context=dict)        

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_exam_view2(request):
    
    dict={
        "courses":Course.objects.filter(course_name="english"),
        "stud":Studentt.objects.get(user_id=request.user.id)
        
    }
    return render(request,'student/student_exam.html',context=dict)

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_exam_view1(request):
    
    dict={
        "courses":Course.objects.filter(course_name="hindi"),
        "stud":Studentt.objects.get(user_id=request.user.id)
        
    }
    return render(request,'student/student_exam.html',context=dict)

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def take_exam_view(request,pk):
    course=Course.objects.get(id=pk)
    total_questions=Questiont.objects.all().filter(course=course).count()
    questions=Questiont.objects.all().filter(course=course)
    
    stud=Studentt.objects.get(user_id=request.user.id)
    total_marks=0
    for q in questions:
        total_marks=total_marks + q.marks
    
    return render(request,'student/take_exam.html',{'course':course,'total_questions':total_questions,'total_marks':total_marks,"stud":stud})

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def start_exam_view(request,pk):
    course=Course.objects.get(id=pk)
    kk=Course.objects.get(id=pk)
    questions=Questiont.objects.all().filter(course=course)
    paginator = Paginator(questions , 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    stud=Studentt.objects.get(user_id=request.user.id)
    if request.method=='POST':
        pass
    response= render(request,'student/start_exam.html',{'kk':kk,'page_obj':page_obj,'course':course,'questions':questions,"stud":stud})
    response.set_cookie('course_id',course.id)
    return response


@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def calculate_marks_view(request):
    if request.COOKIES.get('course_id') is not None:
        course_id = request.COOKIES.get('course_id')
        course=Course.objects.get(id=course_id)
        total_marks=0
        questions=Questiont.objects.all().filter(course=course)
        for i in range(len(questions)):
            selected_ans = request.COOKIES.get(str(i+1))
            actual_answer = questions[i].answer
            if selected_ans == actual_answer:
                total_marks = total_marks + questions[i].marks
        student = models.Studentt.objects.get(user_id=request.user.id)
        result = Result()
        result.marks=total_marks
        result.exam=course
        result.student=student
        result.save()
        return HttpResponseRedirect('view-result')
        
    


@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def view_result_view(request):
    dict={
        "courses":Course.objects.all(),
        "stud":Studentt.objects.get(user_id=request.user.id)

    }
    return render(request,'student/view_result.html',context=dict)
    

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def check_marks_view(request,pk):
    course=Course.objects.get(id=pk)
    student = models.Studentt.objects.get(user_id=request.user.id)
    results= Result.objects.all().filter(exam=course).filter(student=student)
    stud=Studentt.objects.get(user_id=request.user.id)
    return render(request,'student/check_marks.html',{'results':results,"stud":stud})

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_marks_view(request):
    courses=Course.objects.all()
    stud=Studentt.objects.get(user_id=request.user.id)
    return render(request,'student/student_marks.html',{'courses':courses,"stud":stud})



