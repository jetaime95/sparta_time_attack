from re import fullmatch
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login as loginsession
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        REGEX_PHONE = '010-\d{3,4}-\d{4}'
        if not fullmatch(REGEX_PHONE, phone):
            return render(request, 'signup.html', {'error': '전화번호을 입력해주세요!'})
        else:
            User.objects.create_user(username=username, password=password, phone=phone, address=address)
            return redirect('/login')

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            loginsession(request, user)
            return redirect('/home')
        else:
            return render('login.html')

@login_required      
def home(request):
    user = request.user.is_authenticated
    if user:
        return render(request, 'home.html')
    else:
        return redirect('/login/')