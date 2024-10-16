from django.shortcuts import render, redirect
from .models import Todolist
from .forms import TodoListForm
from django.views.decorators.http import require_POST

def index(request):
    todo_items = Todolist.objects.order_by('id')
    form = TodoListForm()
    context = {'todo_items': todo_items, 'form': form}
    return render(request, 'todolist/index.html', context)

@require_POST
def addTodoItem(request):
    form = TodoListForm(request.POST)
    if form.is_valid():
        form.save()  # Save the new todo item to the database
    return redirect('index')

def completedTodo(request, todo_id):
    todo = Todolist.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')

def deleteCompleted(request):
    Todolist.objects.filter(completed=True).delete()
    return redirect('index')

def deleteAll(request):
    Todolist.objects.all().delete()
    return redirect('index')
