from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from todoapp.forms import TodoCreateForm
from .models import Todos,SubTask,Course,Student,StudentCourse
from .forms import Todos,SubTaskForm,CourseForm,StudentForm,StudentCourseMultiForm
from collections import defaultdict


# Create your views here.\

def index(request):
    return render(request,'index.html')
    
def create_todo(request):
        form = TodoCreateForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('list')
        return render(request, 'createtodo.html', {'form': form})
    

def list_all_todos(request):
    todos = Todos.objects.all()  
    context = {"todos": todos}
    return render(request, 'listalltodos.html', context)
     

def edit_todo(request,pk):
     instance_edit=Todos.objects.get(pk=pk)
     
     if request.POST:
         frm=TodoCreateForm(request.POST,instance=instance_edit)

         if frm.is_valid():
          instance_edit.save()
         return redirect("list")
     
     else:  
         form=TodoCreateForm(instance=instance_edit)
     return render(request,"createtodo.html",{'form': form})



def delete_todo(request,pk):
   instance = Todos.objects.get(pk=pk)
   instance.delete()
   return redirect("list")


def create_subtask(request):
    if request.method == 'POST':
        form=SubTaskForm(request.POST)
        if form.is_valid():
            subtask=form.save(commit=False)
            subtask.save()
            form.save_m2m()
            return redirect('subtask_list')
    else:
        form=SubTaskForm()
    return render(request,'subtask.html',{'form':form})

def delete_subtask(request,pk):
   instance = SubTask.objects.get(pk=pk)
   instance.delete()
   return redirect("subtask_list")

# def edit_subtask(request,pk):
#     subtask=get_object_or_404(SubTask,pk=pk)

#     if request.method=="POST":
#         form=SubTaskForm(request.POST,instance=subtask)
#         if form.is_valid():
#           subtask = form.save(commit=False)
#           subtask.save()
#           form.save_m2m()
#           return redirect('subtask_list')  
#         else:
#             form=SubTaskForm(instance=subtask)
#         return render(request,'subtask.html',{'form':form})

def subtask_list(request):
    subtasks = SubTask.objects.prefetch_related('task_name').all()
    return render(request, 'subtask_list.html', {'subtasks': subtasks})



def course_create(request):
    form=CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('course_list')
    return render(request,'course_create.html',{'form':form})

def course_list(request):
    courselist = Course.objects.all()
    return render(request,'course_list.html',{'courselist':courselist})

def course_edit(request,pk):
    course=get_object_or_404(Course,pk=pk)
    form=CourseForm(request.POST or None, instance=course)
    if form.is_valid():
        form.save()
        return redirect('course_list')
    return render(request,'course_create.html',{'form':form})

def course_delete(request,pk):
    course=get_object_or_404(Course,pk=pk)
    course.delete()

def create_studentdet(request):
    form=StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request,'createstudent_det.html',{'form':form})

def studentlist(request):
    student = Student.objects.all()  
    return render(request, 'student_list.html', {'student':student})

def enroll_student(request):
    form=StudentCourseMultiForm(request.POST or None)
    if form.is_valid():
        student=form.cleaned_data['student_name']
        courses=form.cleaned_data['course_name']
        for course in courses:
            StudentCourse.objects.create(student_name=student,course_name=course)
        return redirect('enrol_list')
    else:
        form=StudentCourseMultiForm()
    return render(request,'enrol.html',{'form':form})

# def student_enrol_list(request):
#     enrollments = StudentCourse.objects.select_related('student_name', 'course_name')
#     return render(request, 'enrol_list.html', {'enrollments': enrollments})

# def student_enrol_list(request):
#     enrollments = StudentCourse.objects.select_related('student_name', 'course_name')

#     grouped_enrollments = defaultdict(list)
#     for enrollment in enrollments:
#         grouped_enrollments[enrollment.student_name].append(enrollment.course_name.course_name)

#     return render(request, 'enrol_list.html', {'grouped_enrollments': grouped_enrollments})

def student_enrol_list(request):
    grouped_enrollments = {}

    for student in Student.objects.all():
        # Filter courses via StudentCourse
        courses = Course.objects.filter(studentcourse__student_name=student)
        grouped_enrollments[student.student_name] = [course.course_name for course in courses]

    return render(request, 'enrol_list.html', {
        'grouped_enrollments': grouped_enrollments
    })
# def student_enrol_list(request):
#     # Get only actual enrollments (rows in StudentCourse)
#     enrollments = StudentCourse.objects.select_related('student_name', 'course_name')

#     grouped_enrollments = defaultdict(list)
#     for enrollment in enrollments:
#         grouped_enrollments[enrollment.student_name].append(enrollment.course_name.course_name)

#     return render(request, 'enrol_list.html', {'grouped_enrollments': grouped_enrollments})

def maxProfit(prices):
    min_price=float('inf')
    max_profit=0

    for price in prices:
        if price<min_price:
            min_price=price
        else:
            max_profit=max(max_profit,price-min_price)
    return max_profit

def max_profit_view(request):
    result = None
    if request.method == 'POST':
        price_str = request.POST.get('prices', '')
        try:
            prices = list(map(int, price_str.split(',')))
            result = maxProfit(prices)  # ✅ just call the function and store result
        except:
            result = "Invalid input"
    return render(request, 'profit.html', {'result': result})

