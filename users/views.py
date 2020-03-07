from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import User

app_name = 'users'

def index(request):
    return HttpResponse("Hello, you're in the User index")

def detail(request, user_id):
    return HttpResponse("You're looking at user %s." % user_id)

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
