from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Profile
from django.contrib.auth.models import User
import random
import datetime
import numpy
import time

global impares
global pares
impares = [] 
pares = []
for i in range(99):
    if i%2==0:
        pares.append(i)
    else:
        impares.append(i)
# Create your views here.
def index(request):
    return render(request, 'clients/index.html')

def login(request):
    return render(request, 'registration/login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            Profile.objects.create(user=user,number=0)
            return redirect('/')
    else:
        form = UserCreationForm()

    context = { 'form' : form }
    return render(request, 'registration/register.html', context)

def NumberLoop(request):  
    user = request.user
    profile = Profile.objects.get(user=user)
    
    hora1 = datetime.datetime.now()
    if profile.number == 0:
        context = {
            'number': 0
        }
        while True:
            for i in numpy.arange(0.5):
                profile.number+=1
                time.sleep(0.5)
                hora = str(datetime.datetime.now())
                profile.log['time'] = hora[:16]
                profile.log['valorAtual'] = profile.number
                profile.log['incremento'] = 1
                profile.log['type'] = 'None'
            hora2 = datetime.datetime.now()
            diferenca = str(hora2 - hora1)
            profile.loglist.append(profile.log.copy())
            profile.save()
            randomNumb = random.randint(3,6)
            if int(diferenca[6])==randomNumb:
                break
        return render(request, 'clients/profile.html', context)
    
    while True:      
        loop(request)
        context = {
            'profile': profile,
            'number': profile.number
        }
        return render(request, 'clients/profile.html', context)


def loop(request):
    global impares
    global pares
    user = request.user
    profile = Profile.objects.get(user=user)


    options = ["PAR","ÍMPAR"]

    which = random.choice(options)
    randomNumb = random.randint(3,6)
    for c in range(randomNumb):    
        if which == "PAR":
            newNumber = random.choice(pares)
            profile.log['incremento'] = newNumber
            profile.log['type'] = which
        elif which == "ÍMPAR":
            newNumber = random.choice(impares)
            profile.log['incremento'] = newNumber
            profile.log['type'] = which
        for c in range(randomNumb*2):
            profile.number+=newNumber
            profile.log['valorAtual'] = profile.number
            hora = str(datetime.datetime.now())
            profile.log['time'] = hora[:19]
            time.sleep(0.5)
            profile.loglist.append(profile.log.copy())
            profile.save()
        time.sleep(1)

def logView(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    context = {
        'profile': profile
    }

    return render(request, 'clients/log.html', context)