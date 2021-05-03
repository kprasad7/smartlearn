from django import forms
from .models import Questions
from . import models
from app1_test.models import Questiont , Course
from app1_test import models

class TestForm(forms.ModelForm):
    class Meta:
        model=Questions
        fields="__all__"
class TestcForm(forms.ModelForm):
    class Meta:
        model=Course
        fields="__all__"        

class QuestionForm(forms.ModelForm):
    
    #this will show dropdown __str__ method course model is shown on html so override it
    #to_field_name this will fetch corresponding value  user_id present in course model and return it
    courseID=forms.ModelChoiceField(queryset=models.Course.objects.all(),empty_label="Course Name", to_field_name="id")
    class Meta:
        model=models.Questiont
        fields=['marks','question','option1','option2','option3','option4','answer']
        widgets = {
            'question': forms.Textarea(attrs={'rows': 3, 'cols': 50})
        }        