from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,'index.html')
def personal(request):
    return render(request,"personal.html")

def signuppage(request):
    if request.method == "POST":
        username = request.POST.get('name').strip()
        password = request.POST.get('password').strip()
        email = request.POST.get('email').strip()

        if not username or not password or not email:
            messages.error(request, "Please fill in all fields")
            return redirect('/')

        user = User.objects.filter(email=email)
        if user.exists():
            messages.error(request, "Email Already in use")
            return redirect('/')

        user = User.objects.create(
            username=username,
            email=email
        )
        user.set_password(password)
        user.save()

        return redirect('/loginpage/')
    return render(request, "signup.html")

def loginpage(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        email = email.strip()

        if not email:
            messages.error(request, "Please enter your email")
            return redirect('/loginpage/')

        user = authenticate(email=email, password=password)
        if user is None:
            messages.error(request, "Invalid email or password")
            return redirect('/loginpage/')
        else:
            login(request, user)
            return redirect('/personal/')

    return render(request, "login.html")  

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def profile(request):
    return render(request,'profile.html')