from django.urls import path
from . import views

urlpatterns = [
    path("", views.todo_list, name="todo_list"),
    path("delete/<int:todo_id>/", views.todo_delete, name="todo_delete"),
    path("edit/<int:todo_id>/", views.todo_edit, name="todo_edit"),
    path("toggle/<int:todo_id>/", views.todo_toggle, name="todo_toggle"),
]