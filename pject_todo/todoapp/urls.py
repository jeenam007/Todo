from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index),
    path('create/',views.create_todo,name='create'),
    path('list/',views.list_all_todos,name='list'),
    
    path('edit/<int:pk>/', views.edit_todo, name='edit'),
    path('delete/<int:pk>/',views.delete_todo,name='delete'),
    path('profit',views.max_profit_view,name='profit')
   
   
]
# path('list/<int:pk>/', views.list_all_todos, name='list'),
