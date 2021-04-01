from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Profile
from django.contrib.auth.models import User
import random
import time
import requests 
import datetime

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
            'number': 0,
            'profile': profile
        }
        print(context)
        while True:
            for i in range(1):
                profile.number+=1
                time.sleep(0.5)
                hora = str(datetime.datetime.now())
                profile.log['time'] = hora[:19]
                profile.log['valorAtual'] = profile.number
                profile.log['incremento'] = 1
                profile.log['type'] = 'None'
                hora2 = datetime.datetime.now()
                diferenca = str(hora2 - hora1)
                profile.loglist.append(profile.log.copy())
                profile.save()
                randomNumb = random.randint(3,6)
                print(profile.log)
                if int(diferenca[6])==randomNumb:
                    return render(request, 'clients/profile.html', context)
    else:
        options = ["ÍMPAR","PAR"]  
        which = random.choice(options)
        randomNumb = random.randint(3,6)
        for c in range(randomNumb):    
            if which == "PAR":
                r = requests.get('http://127.0.0.1:8000/par/').json()
                newNumber = r['number']
                print(r)
                profile.log['incremento'] = newNumber
                profile.log['type'] = which
            elif which == "ÍMPAR":
                r = requests.get('http://127.0.0.1:8000/impar/').json()
                print(r)
                newNumber = r['number']
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
                print(profile.log)
            time.sleep(1)
            context = {
                'profile': profile,
                'number': profile.number
            }
            return render(request, 'clients/profile.html', context)

def logView(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    context = {
        'profile': profile
    }

    return render(request, 'clients/log.html', context)