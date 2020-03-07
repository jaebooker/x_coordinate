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

class ProjectFormView(CreateView):
  def get(self, request):
      context = {'form': ProjectForm()}
      return render(request, 'projects/new_project.html', context)

  def post(self, request):
      form = ProjectForm(request.POST)
      if form.is_valid():
          project = form.save()
          return HttpResponseRedirect(reverse_lazy('projects:detail', args=[project.id]))
      return render(request, 'projects/new_project.html', {'form': form})
