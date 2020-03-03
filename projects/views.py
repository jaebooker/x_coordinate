from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    project_list = Project.objects.order_by('-created_on')[:20]
    context = {'project_list': project_list}
    return render(request, 'projects/index.html', context)

def detail(request, project_id):
    return HttpResponse("You're looking at user %s." % project_id)
