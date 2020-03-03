from django.db import models

class User(models.Model):
    joined_on = model.DateTimeField('date created')
    description = models.CharField(max_length=500)
    skills = models.CharField(max_length=200)
    # projects = models.ForeignKey(Project, on_delete=models.CASCADE)
