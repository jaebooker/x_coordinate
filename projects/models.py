from django.db import models
from users.models import User

class Project(models.Model):
    created_on = model.DateTimeField('date created')
    updated_on = model.DateTimeField('date created')
    description = models.CharField(max_length=5000)
    role_number = models.IntegerField(default=0)
    contributers = models.ForeignKey(User, on_delete=models.CASCADE)
