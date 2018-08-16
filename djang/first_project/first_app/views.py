from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request_banana):
  my_dict = {'insert_me': "Hello I am from views.py!"}

  return render(request_banana, 'first_app/index.html', context=my_dict)