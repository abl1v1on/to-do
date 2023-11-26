from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView

from .forms import *
from .models import *


def index(request):
    task = Task.objects.filter(status=1)
    if request.method == "POST":
        form = InputTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = InputTaskForm()
    return render(request, 'list/index.html', {"form": form, 'task': task})


class DeleteTask(DeleteView):
    model = Task
    template_name = 'list/index.html'
    success_url = reverse_lazy('home')


class UpdateTaskStatus(UpdateView):
    # model = Anime
    # fields = "__all__"
    form_class = Task
    template_name = 'list/index.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Task.objects.all()

