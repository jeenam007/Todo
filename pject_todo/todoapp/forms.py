from django import forms 
from django.forms import ModelForm
from .models import Todos

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