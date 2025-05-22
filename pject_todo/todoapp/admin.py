from django.contrib import admin
from .models import Todos, SubTask,Course,Student,StudentCourse

# Basic registration
admin.site.register(Todos)
admin.site.register(SubTask)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(StudentCourse)

