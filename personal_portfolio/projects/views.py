from django.shortcuts import render
from projects.models import Project

def project_index(request):
    projects = Project.objects.all() #массив всех проектов
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)
def project_detail(request, pk):
    project = Project.objects.get(pk=pk) #проект с определенным номером
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)