from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord, Webpage, Topic
# Create your views here.

def index(request_banana):
  webpage_list = AccessRecord.objects.order_by('date')
  date_dict = {
    'access_records': webpage_list,
    'insert_me': "Hello I am from views.py!"
  }
  # my_dict = {'insert_me': "Hello I am from views.py!"}

  return render(request_banana, 'first_app/index.html', context=date_dict)