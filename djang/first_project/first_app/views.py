from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request_banana):
  return HttpResponse('Hello World')