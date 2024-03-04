from django.shortcuts import render
from django.http import HttpResponse

# Add the Task class & list and view function below the imports
class Task:  
  def __init__(self, title, priority, description):
    self.title = title
    self.priority = priority
    self.description = description

tasks = [
  Task('exercise', 'high', '5 set of push up'),
  Task('exercise', 'low', '2 set of push up'),
  Task('exercise', 'mid', '3 set of push up'),
]

# Create your views here.
# home view
def home(request):
  return HttpResponse('<h1>Todo</h1>')

def todo_task(request):
  return render(request, 'todotask.html')

# Add new view
def task_index(request):
  return render(request, 'tasks/index.html', {'tasks': tasks})