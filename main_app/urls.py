from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('todotask/', views.todo_task, name='todo_task'),
  path('tasks/', views.task_index, name='task-index'),
]