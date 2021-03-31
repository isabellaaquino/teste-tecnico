from django.shortcuts import render

# third party imports:
from rest_framework.views import APIView
from rest_framework.response import Response

class ParView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'teste': 'isso é um teste',
            'idade': 23
        }
        return Response(data)

#class ImparView(APIView):
