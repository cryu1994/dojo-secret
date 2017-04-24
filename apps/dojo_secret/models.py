from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def register(self, PostData):
        messages = []
        if len(PostData['first_name']) < 1:
            messages.append("First name is empty.")
        if len(PostData['last_name']) < 1:
            messages.append("Last name is empty.")
        if len(PostData['email']) < 1:
            messages.append("email is empty.")
        if not EMAIL_REGEX.match(PostData['email']):
            messages.append("Invalid Email")
        if len(PostData['password']) < 6:
            messages.append("Password must be longer than 6 letter!.")
        if PostData['conf_password'] != PostData['password']:
            messages.append("Password Not Match!")
        return messages
    def loign(self, login):
        messages = []
        if len(login['email']) < 1:
            messages.append("Enter your Email!")
        if not EMAIL_REGEX.match(login['email']):
            messages.append("Invalid email!")
        if len(login['password']) < 1:
            messages.append("Enter your Password!")

    def verify(self, login):
        if not User.objects.filter(email=login['email']):
            messages.append("Invalid User!")
        else:
            if login['password'] != User.objects.filter(email=login['email']).password:
                messages.append("Incorrect Password!")
        return messages
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=225)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
class Comment(models.Model):
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
class Like(models.Model):
    user_id = models.ForeignKey(User)
    comment_id = models.ForeignKey(Comment)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
