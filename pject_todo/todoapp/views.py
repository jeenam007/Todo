from django.shortcuts import render, redirect
from django.http import HttpResponse
from todoapp.forms import TodoCreateForm
from .models import Todos
from .forms import Todos


# Create your views here.\

def index(request):
    return render(request,'index.html')
    
def create_todo(request):
    if request.method == "GET":
        form = TodoCreateForm()
        return render(request, 'createtodo.html', {'form': form})
  
   
    elif request.method == "POST":
        form = TodoCreateForm(request.POST)
        if form.is_valid():
       
          form.save()
   
        else:
            form=TodoCreateForm
        return render(request,"index.html",{'form': form})


    

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
   todos = Todos.objects.all() 
   context = {"todos": todos}
   return redirect("list")
     
#    return render(request, 'listalltodos.html', context)

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
