from django.shortcuts import render
from appTwo.models import User
# from . import forms
from appTwo.forms import UserRegister
# Create your views here.
def index(request):
  return render(request, 'appTwo/index.html')

def users(request):
  form = UserRegister()
  if request.method == "POST":
    form = UserRegister(request.POST)
    if form.is_valid():
      form.save()
      return index(request)
    else: 
      print("Error form invalid")
  
  return render(request, 'appTwo/register.html',{'form': form})


# def users(request):
#   user_list = User.objects.order_by('first_name')
#   user_dict ={
#     'users': user_list
#   }
#   return render (request, 'appTwo/user.html', context=user_dict)