from django.db import models
from projects.models import Project
from django import forms

class UserForm(forms.Form):
    user_name = forms.CharField(max_length=20)
    description = forms.CharField(max_length=500)
    skills = models.CharField(max_length=200)

class User(models.Model):
    joined_on = model.DateTimeField('date created')
    user_name = model.CharField(max_length=20)
    description = models.CharField(max_length=500)
    skills = models.CharField(max_length=200)
    projects = models.ForeignKey(Project, on_delete=models.CASCADE)
