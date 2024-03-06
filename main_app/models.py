from django.db import models
from django.urls import reverse


# Create models
class Task(models.Model):
  title = models.CharField(max_length=100)
  priority = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse('task-detail', kwargs={'task_id': self.id})