from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^users/login$', views.login),
    url(r'^user/comments$', views.comment),
    url(r'^like/(?P<comment_id>\d+)', views.like),
    url(r'^unlike/(?P<comment_id>\d+)', views.like),
]
