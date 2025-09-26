from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import TODOO

def signup(request):
    if request.method=='POST':
        fnn=request.POST.get('fnn')
        email=request.POST.get('email')
        pwd=request.POST.get('pwd')
        print(fnn,email,pwd)
        my_user=User.objects.create_user(fnn,email,pwd)
        my_user.save()
        return redirect('/login')


    return render(request,'signup.html')

