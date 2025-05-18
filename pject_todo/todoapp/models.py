from django.db import models


class Todos(models.Model):
    task_name = models.CharField(max_length=150)
    status = models.CharField(max_length=25, default="Not Completed")
    user = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)

    

    def __str__(self):
        return self.task_name



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
