from django.shortcuts import redirect, render
from .forms import TodoForm
from .models import Todo

# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()

    if request.method == "POST":
        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("todo_list")
    else:
        form = TodoForm()
    

    return render(request, "todos/list.html", {
        "todos": todos,
        "form" : form,
    })

def todo_delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()

    return redirect("todo_list")

def todo_edit(request, todo_id):
    todo = Todo.objects.get(id=todo_id)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)

        if form.is_valid():
            form.save()
            return redirect("todo_list")
    else:
        form = TodoForm(instance=todo)

    return render(request, "todos/edit.html", {
        "form": form,
        "todo": todo,
    })