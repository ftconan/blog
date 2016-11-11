# coding:utf-8

from django.conf.urls import url, include

import views

urlpatterns = [
	#一级页面
	url(r'^$', views.index),
	url(r'^blog$', views.blog),
	url(r'^album$', views.album),
	url(r'^music$', views.music),
	url(r'^film$', views.film),
	url(r'^share$', views.share),
	url(r'^message$', views.message),

	#二级页面
	url(r'^secondBlog$', views.secondBlog),
	url(r'^secondAlbum$', views.secondAlbum),
	url(r'^secondMusic$', views.secondMusic),
	url(r'^secondFilm$', views.secondFilm),
]