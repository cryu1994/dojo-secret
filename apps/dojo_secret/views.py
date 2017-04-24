from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Comment, Like

def index(request):
    return render(request, "index/index.html")

def register(request):
    req = request.POST
    PostData = {
        'first_name': req['first_name'],
        'last_name': req['last_name'],
        'email': req['email'],
        'password':req['password'],
        'conf_password': req['conf_password']
    }
    errors = User.objects.register(PostData)
    for error in errors:
        messages.error(request, error)

    if not errors:
        user = User.objects.create(first_name = request.POST['first_name'],last_name = request.POST['last_name'],email = request.POST['email'],password = request.POST['password'])
        request.session['user_id'] = user.id
        request.session['name'] = user.first_name
        return redirect('/success')
    request.session['loginError']=False
    return redirect("/")

def login(request):
    req = request.POST
    login = {
        'email': req['email'],
        'password': req['password']
    }
    errors = User.objects.filter(login)
    for error in errors:
        messages.error(request, error)

    if not errors:
        user = User.objects.verify(login)

        return redirect("/success")
    request.session['loginError']=True
    return redirect('/')
def success(request):
    users = User.objects.all()
    context = {
        'user':users
    }
    return render(request, "index/success.html", context)

# Create your views here.
