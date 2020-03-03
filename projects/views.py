from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, you're in the Project index")

def detail(request, project_id):
    return HttpResponse("You're looking at user %s." % project_id)
