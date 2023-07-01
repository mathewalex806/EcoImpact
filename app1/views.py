from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import json
from django.http import JsonResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .models import User , Airtravel , Roadtravel , Seatravel , Info , Energy , Goods
# Create your views here.

def index(request):
    return render(request, "app1/index.html")

def login_view(request):
    if request.method == "POST":
        try:
            username = request.POST["username"]
            password = request.POST["password"]
            q= User.objects.get(username=username)
            if q.password == password:
                return render(request, "app1/main.html", {"username": "username", "q": q})
            else:
                return render(request, "app1/login.html", {"message": "Incorrect password. Try again."})
        except:
            return render(request, "app1/login.html", {"message": "Invalid credentials. Please try again."})
    else:
        return render(request, "app1/login.html")
    
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        q= User.objects.all()
        for i in q:
            if i.username == username:
                return render(request, "app1/register.html", {"message": "Username already taken."})
        user = User(username=username, password=password, email=email)
        user.save()
        return render(request, "app1/login.html", {"message": "User successfully registered."})
    else:
        return render(request, "app1/register.html")
    
def main(request):
    return render(request, "app1/main.html")

def Airtravelf(request):
    q= Airtravel.objects.all()
    return render(request, "app1/Airtravel.html", {"q": q})

def Roadtravelf(request):
    q= Roadtravel.objects.all()
    return render(request, "app1/Roadtravel.html" , {"q": q})

def Seatravelf(request):
    q= Seatravel.objects.all()
    return render(request, "app1/Seatravel.html" , {"q": q})

def Infof(request):
    q = Info.objects.all()
    return render(request, "app1/Info.html" , {"q": q})

def Energyf(request):
    q = Energy.objects.all()
    return render(request, "app1/Energy.html" , {"q": q})

def Goodsf(request):
    q = Goods.objects.all()
    return render(request, "app1/Goods.html" , {"q": q})

def Contributef(request):
    return render(request, "app1/Contribute.html")

def result(request):
    return render(request, "app1/result.html")

def profile(request, username):
    q= User.objects.get(username=username)
    return render(request, "app1/profile.html" , {"q": q})

def logout_view(request):
    logout(request)
    return render(request, "app1/login.html", {"message": "Logged out."})


