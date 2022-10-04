from django.utils import timezone
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm
from .models import Task

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):

    if request.method == 'GET':
        print('Enviando formulario')
        return render(request, 'signup.html',{
        'form' : UserCreationForm
        })
    else:
        print(request.POST)
        print('Obteniendo datos')
        if request.POST['password1'] == request.POST['password2']:
            #register User
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.
                    POST['password1'])
                user.save()
                login(request, user)
                return redirect(tasks)
            except IntegrityError:
                return render(request, 'signup.html',{
                    'form' : UserCreationForm,
                    'error': 'El nombre de usuario ya existe'
                })
        return render(request, 'signup.html',{
            'form' : UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })


def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'tasks.html', {'tasks': tasks})

def tasks_completed(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by
    ('-dateCompleted')
    return render(request, 'tasks.html', {'tasks': tasks})

def createTasks(request):
    
    if request.method == 'GET':
        return render(request, 'createTasks.html', {
            'form': TaskForm
        })
    else: 
        try:
            form = TaskForm(request.POST)
            new_Task = form.save(commit=False)
            new_Task.user = request.user
            new_Task.save()
            return redirect('tasks')
        except ValueError:
          return render(request, 'createTasks.html', {
            'form': TaskForm,
            'error': 'Porfavor ingrese datos válidos'
        })  

def taskDetail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'taskDetail.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'taskDetail.html', {'task': task, 'form': form,
            'error': 'Error al actualizar la tarea'})

def completeTask(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')

def deleteTask(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html',{
            'form':AuthenticationForm
        })
    else:
        print(request.POST)
        user = authenticate(request, username=request.POST['username'], password=request.POST
            ['password'])
        if user is None:
            return render(request, 'signin.html',{
                'form':AuthenticationForm,
                'error': 'El nombre de usuario o contraseña están incorrectos'
            })  
        else:
            login(request, user)
            return redirect('tasks')