from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.shortcuts import HttpResponse,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def SignUp(request):

    if request.method=='POST':
        uname=request.POST.get('username')
        uemail=request.POST.get('email')
        upass1=request.POST.get('password1')
        upass2=request.POST.get('password2')
        
        my_user=User.objects.create_user(uname,uemail,upass1)
        my_user.save()

        return redirect('login')

    return render(request,'SignUp.html')


def LogInpage(request):

    if request.method=='POST':
        uname=request.POST.get('username')
        upass=request.POST.get('pass')

        user=authenticate(request,username=uname,password=upass)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('Username or password incorrect')
    return render(request,'Login.html')


@login_required(login_url='login')
def HomePage(request):
    return render(request,'Home.html')

def Logout(reqest):
    return redirect('login')