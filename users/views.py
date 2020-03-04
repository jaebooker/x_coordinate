from django.shortcuts import render
from django.http import HttpResponse

from .models import User

app_name = 'users'

def index(request):
    return HttpResponse("Hello, you're in the User index")

def detail(request, user_id):
    return HttpResponse("You're looking at user %s." % user_id)
