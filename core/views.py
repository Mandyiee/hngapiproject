from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    obj ={
        "slackUsername": 'Mandy' ,
        "backend": True,
        "age": 20,
        "bio": "I am a passionate web developer"
    }
    
    return JsonResponse(obj)