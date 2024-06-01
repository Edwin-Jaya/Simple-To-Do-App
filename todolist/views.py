from django.shortcuts import render, redirect
from . models import todolist
from . forms import todolistform
from django.contrib import messages

# Create your views here.

def index_view(request):
    return render(request, './index.html')

def dashboard_view(request):
    
    tasks = todolist.objects.all() 
    context = {
        'tasks': tasks
    }
    return render(request, './dashboard.html', context)

def create_form(request):
    
    todolist_form = todolistform()
    if request.method == 'POST':
        todolist_form = todolistform(request.POST)
        if todolist_form.is_valid():
            todolist_form.save()
            messages.success(request, 'Task added successfully')
            return redirect('dashboard')
    else:
        todolist_form = todolistform()
        return render(request, './create_form.html', {'form': todolist_form})
    
    return render(request, './create_form.html')

def update_form(request, pk):
    
    task = todolist.objects.get(id=pk)
    todolist_form = todolistform(instance=task)
    
    if request.method == 'POST':
        todolist_form = todolistform(request.POST, instance=task)
        if todolist_form.is_valid():
            todolist_form.save()
            messages.success(request, 'Task updated successfully')
            return redirect('dashboard')
    else:
        todolist_form = todolistform(instance=task)
    return render(request, './create_form.html', {'form': todolist_form})

def delete_form(request, pk):
    
    task = todolist.objects.get(id=pk)
    task.delete()
    messages.success(request, 'Task deleted successfully')
    
    return redirect('dashboard')