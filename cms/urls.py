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

	#栏目管理
	url(r'^addClassification', load.addClassification),
	url(r'^classificationList', load.classificationList),

	#账户管理
	url(r'^addAccount', load.addAccount),
	url(r'^accountList', load.accountList),

	#图片管理
	url(r'^addPicture', load.addPicture),
	url(r'^pictureList', load.pictureList),
]