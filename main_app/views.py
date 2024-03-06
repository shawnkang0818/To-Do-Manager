from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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
class Home(LoginView):
  template_name = 'home.html'

def todo_task(request):
  return render(request, 'todotask.html')

# Add new view
@login_required
def task_index(request):
  tasks = Task.objects.filter(user=request.user)
  return render(request, 'tasks/index.html', {'tasks': tasks})

# Add detail view
@login_required
def task_detail(request, task_id):
  task = Task.objects.get(id=task_id)
  return render(request, 'tasks/detail.html', { 'task': task })

class TaskCreate(LoginRequiredMixin, CreateView):
  model = Task
  fields = ['title', 'priority', 'description']
  success_url = '/tasks/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
  model = Task
  # Let's disallow the renaming of a task by excluding the name field!
  fields = ['title', 'priority', 'description']

class TaskDelete(LoginRequiredMixin, DeleteView):
  model = Task
  success_url = '/tasks/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # add the user to the database
      user = form.save()
      # log a user in
      login(request, user)
      return redirect('task-index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)