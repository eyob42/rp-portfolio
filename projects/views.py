from django.shortcuts import get_object_or_404, render
from projects.models import Projects

def project_index(request):
    project = Projects.objects.all()
    context = {
        "projects": project
    }
    return render(request, "projects/project_index.html", context)


def project_detail(request, pk):
    project = get_object_or_404(Projects, pk=pk)
    context = {
        "project": project
    }
    return render(request, "projects/project_detail.html", context)