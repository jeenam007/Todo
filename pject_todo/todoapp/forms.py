from django import forms 
from django.forms import ModelForm
from .models import Todos,SubTask,Course,Student,StudentCourse
from django_select2.forms import ModelSelect2MultipleWidget

class TodoCreateForm(ModelForm):
    class Meta:
        model=Todos
        fields='__all__'
    task_name=forms.CharField()
    user=forms.CharField()
    options=(
            ("", "Select Status"),  # Default placeholder option
            ("completed","Completed"),
             ("not_completed","Not completed"))
    status=forms.ChoiceField(choices=options,label="Status")
    def clean(self):
        print("inside clean")

class SubTaskForm(forms.ModelForm):
    class Meta:
        model=SubTask
        fields=['task_name','subtask']
        widgets={
            'task_name':forms.SelectMultiple(),
            'subtask':forms.TextInput(attrs={'class':'form-control'})
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model =Course
        fields=['course_name','course_code']
        widget={
            'course_name':forms.TextInput(attrs={'class':'form-control'}),
            'course_code':forms.TextInput(attrs={'class':'form-control'})
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_name', 'email', 'qualification', 'mobile_no', 'address']
        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),  # changed to EmailInput widget
            'qualification': forms.Select(attrs={'class': 'form-control'}),
            'mobile_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
        }
       

# class StudentCourseForm(forms.ModelForm):
#     class Meta:
#         model=StudentCourse
#         fields=['student_name','course_name']
#         widgets={
#             'student_name':forms.TextInput(attrs={'class':'form-control'}),
#             'course_name':forms.TextInput(attrs={'class':'form-control'}),
            
#         }
class StudentCourseMultiForm(forms.Form):
    student_name=forms.ModelChoiceField(queryset=Student.objects.all())
    course_name=forms.ModelMultipleChoiceField(
     queryset=Course.objects.all(),
     widget=forms.SelectMultiple,  
    )

    


