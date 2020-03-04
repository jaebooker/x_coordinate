from django.db import models
from projects.models import Project

class User(models.Model):
    joined_on = model.DateTimeField('date created')
    user_name = model.CharField(max_length=20)
    description = models.CharField(max_length=500)
    skills = models.CharField(max_length=200)
    projects = models.ForeignKey(Project, on_delete=models.CASCADE)
