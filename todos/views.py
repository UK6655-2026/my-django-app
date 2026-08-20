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