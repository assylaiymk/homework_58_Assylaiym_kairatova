from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from webapp.forms import TaskForm
from webapp.models import Task


def add_view(request):
    form = TaskForm()
    if request.method == 'GET':
        return render(request, 'task_create.html', context={'form': form})
    form = TaskForm(request.POST)
    if not form.is_valid():
        return render(request, 'task_create.html', context={'form': form})
    task = form.save()
    return redirect('task_detail', pk=task.pk)


def detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task.html', context={'task': task})


class TaskView(TemplateView):
    template_name = 'task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from webapp.models import Task
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


class TaskUpdateView(TemplateView):
    template_name = 'task_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = TaskForm(instance=context['task'])
        context['form'] = form
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect('task_detail', pk=task.pk)
        return render(request, 'task_update.html', context={'form': form})


def delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_confirm_delete.html', context={'task': task})


def confirm_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('index')
