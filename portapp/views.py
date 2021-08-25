from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.
def home(request):
    projects = Project.objects.all()

    return render(request, 'portapp/index.html', {'projects': projects})

def detail(request, skill_id):
    skill = get_object_or_404(Project, pk=skill_id)
    return render(request, 'portapp/detail.html', {'skill':skill})
