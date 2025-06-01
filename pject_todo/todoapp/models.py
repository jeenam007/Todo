from django.db import models
from django.utils import timezone


class Todos(models.Model):
    task_name = models.CharField(max_length=150)
    status = models.CharField(max_length=25, default="Not Completed")
    user = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return self.task_name
    
class SubTask(models.Model):
        # task_name = models.ForeignKey(Todos, on_delete=models.CASCADE, null=True, blank=True)   
        task_name = models.ManyToManyField('Todos')
        subtask = models.CharField(max_length=25)
        created_date = models.DateTimeField(default=timezone.now)

        def __str__(self):
            return self.subtask
      


class Course(models.Model):
     course_name=models.CharField(max_length=100)
     course_code=models.CharField(max_length=15,unique=True)
     def __str__(self):
            return self.course_name
          
        #   return f"{self.course_name}-{self.course_code}"
     
class Student(models.Model):
    QUALIFICATION_CHOICES = (
        ("", "Select"),
        ('BTech', 'BTech'),
        ('BBA', 'BBA'),
        ('BCA', 'BCA'),
        ('MBA', 'MBA'),
        ('MTech', 'MTech'),
    )

    student_name = models.CharField(max_length=100,null=False,blank=False)
    email = models.EmailField(unique=True,null=False,blank=False)
    qualification = models.CharField(
        max_length=10,  # Choices are short; 10 is enough
        choices=QUALIFICATION_CHOICES,
        blank=False,
        null=False
    )
    mobile_no = models.BigIntegerField(blank=True, null=True)
    address = models.CharField(max_length=300, blank=False, null=True)

    def __str__(self):
        return self.student_name
     
class StudentCourse(models.Model):
     student_name=models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)  
     course_name=models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
     enrolled_on=models.DateField(auto_now_add=True)

     class Meta:
        unique_together=('student_name', 'course_name')
     def __str__(self):
          return f"{self.student_name}-{self.course_name}"
        #   return f"{self.student_name}-{self.course_name.course_code}"
    



#ORM query for creating an object
#reference_name=className(fieldname=value,fieldname=value,fieldname=value)
#reference.save
#todo=Todos(task_name="Gas Payment",status="Not Completed",user="Sinu")
#todo.save()
#python manage.py shell

#ORM query for fetching all records
#reference_name=className.objects.all()
#todo=Todos.objects.all()
#print(print)

#todos created by a user
#ref_name=modelname.objects.filter(field=value)
#todos=Todos.objects.filter(user="QA")