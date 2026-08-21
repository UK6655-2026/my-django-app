from django.shortcuts import redirect, render, get_object_or_404
from .forms import TodoForm
from .models import Todo
from django.contrib.auth.decorators import login_required


@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)

    if request.method == "POST":
        form = TodoForm(request.POST)

        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()

            return redirect("todo_list")
    else:
        form = TodoForm()

    return render(request, "todos/list.html", {
        "todos": todos,
        "form": form,
    })


@login_required
def todo_delete(request, todo_id):
    todo = get_object_or_404(
        Todo,
        id=todo_id,
        user=request.user
    )

    todo.delete()

    return redirect("todo_list")


@login_required
def todo_edit(request, todo_id):
    todo = get_object_or_404(
        Todo,
        id=todo_id,
        user=request.user
    )

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


@login_required
def todo_toggle(request, todo_id):
    todo = get_object_or_404(
        Todo,
        id=todo_id,
        user=request.user
    )

    todo.completed = not todo.completed
    todo.save()

    return redirect("todo_list")