# coding=utf-8

from django.conf.urls import url
import views
import load

urlpatterns = [
	#登录界面
	url(r'^login$', views.login),
	url(r'^logout$', views.logout),

	#仪表盘
	url(r'^dashboard', load.dashboard),

	#发布博文
	url(r'^addNews', load.addNews),
	url(r'^newsList', load.newsList),
]