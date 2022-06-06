from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=800)
    created = models.DateTimeField(auto_now_add=True)