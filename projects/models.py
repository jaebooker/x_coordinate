from django.db import models
from users.models import User
from django import forms

class ProjectForm(forms.Form):
    title= forms.CharField(max_length=20)
    description = forms.CharField(max_length=5000)
    number_of_roles = models.IntegerField(default=0)

class Project(models.Model):
    created_on = model.DateTimeField('date created')
    updated_on = model.DateTimeField('date created')
    title = mode.CharField(max_length=20)
    description = models.CharField(max_length=5000)
    number_of_roles = models.IntegerField(default=0)
    roles_filled = models.IntegerField(default=1)
    contributers = models.ForeignKey(User, on_delete=models.CASCADE)
