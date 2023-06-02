from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from . import forms
from . import models


# Create your views here.
class ProjecListViews(ListView):
    model = models.Project
    template_name = 'project/list.html'

class ProjectCreateView(CreateView):
    model = models.Project
    form_class = forms.ProjectCreateForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('Project_List')
