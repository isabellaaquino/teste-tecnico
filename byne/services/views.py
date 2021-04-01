from django.shortcuts import render
import random
import datetime
# third party imports:
from rest_framework.views import APIView
from rest_framework.response import Response

global impares
global pares

impares = [] 
pares = []
for i in range(99):
    if i%2==0:
        pares.append(i)
    else:
        impares.append(i)
def ParGen():
    number = random.choice(pares)
    return number
def ImparGen():
    number = random.choice(impares)
    return number

class ParView(APIView):
    def get(self, request, *args, **kwargs):
        time = str(datetime.datetime.now())
        timefinal = time[:19]
        data = {
            'number': ParGen(),
            'type': 'PAR' ,
            'time': timefinal       
        }
        return Response(data)

class ImparView(APIView):
    def get(self, request, *args, **kwargs):
        time = str(datetime.datetime.now())
        timefinal = time[:19]
        data = {
            'number': ImparGen(),
            'type': 'IMPAR',
            'time': timefinal
        }
        return Response(data)