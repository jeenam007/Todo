from django.urls import path
from . import views
urlpatterns = [
    path('todoapi/', views.todo_vw, name='gettodolist'),#GET http://127.0.0.1:8000/api/v1todoapi/
    path('tododetail/<int:id>/',views.todo_edit,name='gettododetail'), # Get http://127.0.0.1:8000/api/v1tododetail/2
    # path('todetail/<int:id>/',views.book_detail,name='getbookdetail'), POST http://127.0.0.1:8000/api/v1todoapi/
    
]