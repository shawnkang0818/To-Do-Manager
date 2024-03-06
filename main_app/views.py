from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Task

# Add the Task class & list and view function below the imports
# class Task:  
#   def __init__(self, title, priority, description):
#     self.title = title
#     self.priority = priority
#     self.description = description

# tasks = [
#   Task('exercise', 'high', '5 set of push up'),
#   Task('exercise', 'low', '2 set of push up'),
#   Task('exercise', 'mid', '3 set of push up'),
# ]

# Create your views here.
# home view
def home(request):
  return render(request, 'home.html')

def todo_task(request):
  return render(request, 'todotask.html')

# Add new view
def task_index(request):
  tasks = Task.objects.all()
  return render(request, 'tasks/index.html', {'tasks': tasks})

# Add detail view
def task_detail(request, task_id):
  task = Task.objects.get(id=task_id)
  return render(request, 'tasks/detail.html', { 'task': task })

class TaskCreate(CreateView):
  model = Task
  fields = '__all__'
  success_url = '/tasks/'