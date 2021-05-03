from django.shortcuts import render , HttpResponseRedirect
from .models import Questions
from .forms import TestForm , QuestionForm,TestcForm 
from app2_student.models import Studentt
#from app2_testcourse.models import Questiont , Course
from app1_test.models import Questiont , Course

def qapost(request):
    if request.method == "POST":
        form = TestForm(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, "questionmake.html", {'form': form})
    else:
        form = TestForm()

    return render(request, "questionmake.html", {'form': form})   

def cpost(request):
    if request.method == "POST":
        form = TestcForm(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, "course.html")
    else:
        form = TestcForm()

    return render(request, "course.html")   




def javaform(request):
    datt=Questions.objects.all()
    questionForm=QuestionForm()
    my_dict = {"Questionss":datt , 'questionForm':questionForm}
    if request.method=='POST':
        questionForm=QuestionForm(request.POST)
        if questionForm.is_valid():
            question=questionForm.save(commit=False)
            course=Course.objects.get(id=request.POST.get('courseID'))
            question.course=course
            question.save()       
        else:
            print("form is invalid")
        return render(request,'addq.html')
    return render(request,'addq.html'  , context=my_dict )
    
    


           



    
            
         