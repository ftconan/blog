# coding:utf-8

from django.conf.urls import url, include

import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^blog$', views.blog),
	url(r'^blog_post$', views.blog_post),
]