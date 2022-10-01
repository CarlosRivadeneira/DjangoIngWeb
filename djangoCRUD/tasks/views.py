from distutils.log import error
from turtle import title
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

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
                return HttpResponse('Usuario creado exitosamente')
            except:
                return render(request, 'signup.html',{
                    'form' : UserCreationForm,
                    'error': 'El nombre de usuario ya existe'
                })
        return render(request, 'signup.html',{
            'form' : UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })
