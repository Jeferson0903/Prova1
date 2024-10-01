from django.shortcuts import render
from .models import Todo

def todo_list(request):
    todos = Todo.objects.all()  # Obtém todos os objetos Todo
    return render(request, 'todos/todo_list.html', {'todos': todos})
