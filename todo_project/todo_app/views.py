from django.shortcuts import render,redirect
from .forms import TaskForm
from .models import TaskModel

# Create your views here.
def home(request):
    return render(request,'home.html')

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_Tasks')
    else:
        form = TaskForm()
    return render(request,'add_task.html',{'form':form})

def show_tasks(request):
    # tasks = TaskModel.objects.all()
    tasks = TaskModel.objects.filter(is_completed=False)
    # for task in tasks:
    #     print(task.taskDescription)
    return render(request,'show_tasks.html',{'tasks':tasks})

def delete_task(request,id):
    task = TaskModel.objects.get(pk=id)
    task.delete()
    # print(task)
    return redirect('show_Tasks')

def edit_task(request,id):
    task =TaskModel.objects.get(pk=id)
    form = TaskForm(request.POST,instance=task)
    if request.method == 'POST':
        task = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_Tasks')
    else:
        form =TaskForm(instance=task)
    return render(request,'add_task.html',{'form':form})

def complete_task(request,id):
    task = TaskModel.objects.get(pk=id)
    task.is_completed=True
    task.save()
    tasks = TaskModel.objects.all()
    return render(request,'completed_tasks.html',{'tasks':tasks})


def completed_tasks(request):
    tasks = TaskModel.objects.filter(is_completed=True)
    return render(request,'completed_tasks.html',{'tasks':tasks})
            