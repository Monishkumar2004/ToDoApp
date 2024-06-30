from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
# def add(request):
    # if request.method == 'POST':
    #     name = request.POST.get('name', '')
    #     priority = request.POST.get('priority', '')

    #     task = Task(name = name, priority = priority)
    #     task.save()

    # return render(request, 'app/add.html')

def view_tasks(request):
    task = Task.objects.all()
    context = {
        'tasks': task
    }
    if request.method == 'POST':
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')

        task = Task(name = name, priority = priority)
        task.save()

    # return render(request, 'app/add.html')
    

    return render(request, 'app/view.html', context)


def delete_task(request, taskid):
    task = Task.objects.get(id = taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'app/delete.html')


def update(request, taskid):
    task = Task.objects.get(id = taskid)
    form = TaskForm(request.POST or None, instance = task)
    context = {
        'form': form,
        'task': task
    }
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'app/edit.html', context )

