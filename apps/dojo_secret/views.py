from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Comment
from django.db.models import Count

def index(request):
    return render(request, "index/index.html")
def register(request):
    PostData = {
        'first_name': request.POST['first_name'],
        'last_name': request.POST['last_name'],
        'email': request.POST['email'],
        'password': request.POST['password'],
        'conf_password': request.POST['conf_password']
    }
    if not User.objects.register(PostData):
        new_user_id = User.objects.create_user(PostData)
        request.session['user_id'] = new_user_id
        request.session['name'] = new_user.first_name
        return redirect("/success")
    for error in User.objects.register(PostData):
        messages.error(request, error)
    request.session['loginError']=False
    return redirect('/')
def login(request):
    PostData = {
        'email': request.POST['email'],
        'password': request.POST['password']
    }
    if not User.objects.login(PostData):
        user_id = User.objects.get(email=PostData['email']).id
        request.session['user_id'] = user_id
        return redirect('/success')
    for error in User.objects.login(PostData):
        messages.error(request, error)
    request.session['loginError']=True
    return redirect('/')
def comment(request):
    PostData = {
        'comment': request.POST['comment'],
        'user_id':request.session['user_id'],
    }
    Comment.objects.add_comment(PostData)
    return redirect('/success')
def success(request):
    if 'user_id' in request.session:
        first_name = User.objects.get(id=request.session['user_id']).first_name
        comments = Comment.objects.all().order_by('-created_at').annotate(num_likes=Count('likes'))
        liked_comments = Comment.objects.filter(likes__id=request.session['user_id'])
        arr = []
        for liked_comment in liked_comments:
            arr.append(liked_comment.id)
        context = {
            'first_name': first_name,
            'comments': comments,
            'messages': messages,
            'arr':arr,
        }
        return render(request, "index/success.html", context)
    messages.error(request, 'You are not logged in!')
    return redirect('/')
def like(request, comment_id):
    PostData = {

        'comment_id': comment_id,
        'user_id': request.session['user_id']
    }
    Comment.objects.like(PostData)
    return redirect('/success')
def unlike(request, comment_id):
    PostData = {
        'comment_id': comment_id,
        'user_id': request.session['user_id']
    }
    Comment.objects.unlike(PostData)
    return redirect('/success')
