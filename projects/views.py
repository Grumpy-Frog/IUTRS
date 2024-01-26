from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from .models import Our_Project
from .forms import Our_ProjectForm


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import markdown

# Create your views here.
def index(request):
    projects = Our_Project.objects.all()
    context = {'projects': projects}

    return render(request, 'projects/index.html', context)


def detail(request, pk):
    projects = Our_Project.objects.get(pk=pk)
    context = {'projects': projects}

    return render(request, 'projects/detail.html', context)



def create_projects(request):
    form = Our_ProjectForm

    if request.method == 'POST':
        form = Our_ProjectForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect("projects:projects")

    context = {'form': form}

    return render(request, 'projects/create_projects.html',context)


class editOur_project(TemplateView):
    template_name = 'projects/edit_projects.html'

    def get_context_data(self, *args, **kwargs):
        projects = Our_Project.objects.get(pk=self.kwargs.get('pk'))
        context = super().get_context_data(*args, **kwargs)

        context['form'] = Our_ProjectForm(instance=projects)
        context['projects'] = projects

        return context




def updateOur_project(request, *args, **kwargs):
    pk = kwargs.get('pk')

    projects = Our_Project.objects.get(pk=pk)

    title = request.POST['title']

    content = request.POST['content']

    projects.title = title
    projects.content = content

    projects.save()

    return HttpResponseRedirect(
        reverse("projects:projects"))



def delete_projects(request, *args, **kwargs):
    pk = kwargs.get('pk')
    d_our_project = Our_Project.objects.get(pk=pk)
    d_our_project.delete()

    return HttpResponseRedirect(
        reverse("projects:projects"))




