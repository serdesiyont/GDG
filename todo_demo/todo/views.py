from django.shortcuts import render, redirect
from .models import TodoItem

def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

def todo_create(request):
    if request.method == 'POST':
        content = request.POST['content']
        TodoItem.objects.create(content=content)
        return redirect('todo_list')
    return render(request, 'todo/todo_create.html')

def todo_complete(request, todo_id):
    todo = TodoItem.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('todo_list')

def todo_delete(request, todo_id):
    todo = TodoItem.objects.get(pk=todo_id)
    todo.delete()
    return redirect('todo_list')