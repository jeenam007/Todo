from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index),
    path('create/',views.create_todo,name='createtodo'),
    path('list/',views.list_all_todos,name='list'),
    
    path('edit/<int:pk>/', views.edit_todo, name='edit'),
    path('delete/<int:pk>/',views.delete_todo,name='delete'),
    path('createsubtask/',views.create_subtask,name='subtask_create'),
    path('subtasklist/',views.subtask_list,name='subtask_list'),
    path('profit',views.max_profit_view,name='profit'),
    path('deletesubtask/<int:pk>/',views.delete_subtask,name='subtask_delete'),
    path('createcourse/',views.course_create,name='course_create'),
    path('listcourse/',views.course_list,name='course_list'),
    path('course_edit/<int:pk>/',views.course_edit,name='course_edit'),
    path('course_delete/<int:pk>/',views.course_delete,name='course_delete'),
    path('createstudent_det',views.create_studentdet,name='createstudent_detail'),
    path('studentslist/',views.studentlist,name='student_list'),
    path('editstudent/<int:pk>/',views.student_edit,name='edit_student'),
    path('enrolstudents/',views.enroll_student,name='enrol_students'),
    path('enrol_list/',views.student_enrol_list,name='enrol_list'),
    path('deletestudent/<int:pk>/',views.delete_student,name='delete_student')
    
   
]
# path('list/<int:pk>/', views.list_all_todos, name='list'),
