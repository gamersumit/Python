from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature
# Create your views here
def index(request):
    features = Feature.objects.all # feature will be a list of all objects ot Feature class in our models.py
    return render(request, 'index.html', {'features': features})

def counter(request):
    posts = [1,2,3,4,'tim', 'tom']
    return render(request, 'counter.html', {'posts': posts})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if (not username) or (not email) or (not password) or (not password2) :
            messages.error(request, 'All fields are required')
            return redirect('register')
        
        elif password == password2 :
            if User.objects.filter(email = email).exists() :
                messages.info(request, 'Email already exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists() :
                messages.info(request, 'Username already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email= email, password=password)
                user.save();
                return redirect('login')
            
        else :
            messages.info(request, 'Password did\'nt match')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
   if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)

        if user :
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials invalid')
            return redirect('login')

   else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def post(request, pk):
    return render(request, 'post.html', {'pk': pk})