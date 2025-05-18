from django.shortcuts import render
from .serializers import todoSerializer
from todoapp.models import Todos
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def todo_vw(request):
    if request.method == 'GET':
        todo=Todos.objects.all()
        serializer=todoSerializer(todo,many=True)
        return JsonResponse(serializer.data,safe=False)
    
    elif request.method == 'POST':
        data=JSONParser().parse(request)
        serializer=todoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=200)
        else:
            return JsonResponse(serializer.errors,status=404)
        

def todo_edit(request,id):
    try:
        todo=Todos.objects.get(id=id)
    except Todos.DoesNotExist:
        return JsonResponse({'error':'Todo not found'},status=404)
       
    
    
    if request.method == "GET":
        serializer=todoSerializer(todo)
        return JsonResponse(serializer.data,status=200,safe=False)
    elif request.method == "PUT":
        data=JSONParser().parse(request)
        serializer=todoSerializer(instance=todo,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=200)
        else:
            return JsonResponse(serializer.errors,status=400)