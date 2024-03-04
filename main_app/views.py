from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# home view
def home(request):
  return HttpResponse('<h1>Todo</h1>')

def todo_task(request):
  return render(request, 'todotask.html')