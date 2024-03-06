from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('todotask/', views.todo_task, name='todo-task'),
  path('tasks/', views.task_index, name='task-index'),
  path('tasks/<int:task_id>/', views.task_detail, name='task-detail'),
  path('tasks/create/', views.TaskCreate.as_view(), name='task-create'),
  path('tasks/<int:pk>/update/', views.TaskUpdate.as_view(), name='task-update'),
  path('tasks/<int:pk>/delete/', views.TaskDelete.as_view(), name='task-delete'),
  path('accounts/signup/', views.signup, name='signup'),
]