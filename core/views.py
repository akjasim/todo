from django.shortcuts import render, redirect
from core.forms import TodoForm
from core.models import Todo


def home(request):
    form = TodoForm()
    todos = Todo.objects.all()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'core/home.html', {'form': form, 'todos': todos})


def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'core/update.html', {'form': form, 'todo': todo})


def delete(request, todo_id):
    if request.method == 'POST':
        Todo.objects.get(id=todo_id).delete()
        return redirect('home')
