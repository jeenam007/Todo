from django import forms 
from django.forms import ModelForm
from .models import Todos,SubTask,Course,Student,StudentCourse
from django_select2.forms import ModelSelect2MultipleWidget


class TodoCreateForm(ModelForm):
    class Meta:
        model=Todos
        fields='__all__'
       
    task_name=forms.CharField(label='Task Name*')
    user=forms.CharField(label='User*')
    options=(
            ("", "Select Status"),  # Default placeholder option
            ("completed","Completed"),
             ("not_completed","Not completed"))
    status=forms.ChoiceField(choices=options,label="Status*")
    def clean(self):
        print("inside clean")

class ExcelUploadForm(forms.Form):
    file = forms.FileField(label="Upload Excel File")

class SubTaskForm(forms.ModelForm):
    class Meta:
        model=SubTask
        fields=['task_name','subtask']
        labels={
          'task_name':'Task Name*',
          'subtask'  :'Sub Task*',
        }
        widgets={
            'task_name':forms.SelectMultiple(),
            # 'task_name': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'subtask':forms.TextInput(attrs={'class':'form-control'})
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model =Course
        fields=['course_name','course_code']
        labels = {
            'course_name': 'Course Name*',
            'course_code': 'Course Code*',
        }
        widget={
            'course_name':forms.TextInput(attrs={'class':'form-control'}),
            'course_code':forms.TextInput(attrs={'class':'form-control'})
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_name', 'email', 'qualification', 'mobile_no', 'address']
        labels={
            'student_name':'Student Name*',
            'email':'Email*',
            'qualification':'Qualification*',
            'mobile_no':'Mobile No.',
            'address':'Address*',
        }
        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control','style': 'width: 450px;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','style': 'width: 450px;'}),  # changed to EmailInput widget
            'qualification': forms.Select(attrs={'class': 'form-control','style': 'width: 450px;'}),
            'mobile_no': forms.NumberInput(attrs={'class': 'form-control','style': 'width: 450px;'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'style': 'width: 450px; height: 200px;'}),
        }
    # def __init__(self, *args, **kwargs):
    #     super(StudentForm, self).__init__(*args, **kwargs)
    #     self.fields['qualification'].choices = [('', 'Select')] + list(self.fields['qualification'].choices) 
       

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

    


