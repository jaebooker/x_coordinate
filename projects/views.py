from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Project

def index(request):
    project_list = Project.objects.order_by('-created_on')[:20]
    context = {'project_list': project_list}
    return render(request, 'projects/index.html', context)

def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/detail.html', {'project': project})
