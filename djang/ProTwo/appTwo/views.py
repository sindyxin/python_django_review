from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
  return HttpResponse("<em>Hello this is second app</em>")
def help(request):
  my_dict ={
    "help": "This  is help page"
  }
  return render (request, "appTwo/help.html", context=my_dict)