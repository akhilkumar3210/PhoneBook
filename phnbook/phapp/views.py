from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def ph_login(req):
    if 'user' in req.session:
        return redirect(phnbook)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        user=authenticate(username=uname,password=password)
        if user:
            login(req,user)
            return redirect(phnbook)
        else:
            messages.warning(req,'Invaild username or password!!!')
            return redirect(phnbook)
    else:
        return render(req,'login.html')
    
    

def register(req):
    if req.method=='POST':
        email=req.POST['email']
        uname=req.POST['uname']
        password=req.POST['password']
        try:
            data=User.objects.create_user(first_name=uname,email=email,username=email,password=password)
            data.save()
            return redirect(ph_login)
        except:
            messages.warning(req,'Email Already Exists!!')
            return redirect(register)
    return render(req,'user/register.html')


def phnbook(req):
    return render(req,'user/phnbook.html')