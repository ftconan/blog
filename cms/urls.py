# coding=utf-8

from django.conf.urls import url

import load
import views
from addNewsViews import saveNews
from addClassificationViews import getClassification, saveClassification
from addAccountViews import saveAccount
from addPictureViews import getPicturePosition, savePicture
from classificationListViews import getClassificationList, deleteClassification
from accountListViews import getAccountList, deleteAccount, getUserName
from pictureListViews import getPictureList, deletePicture

urlpatterns = [
	#登录界面
	url(r'^login$', views.login),
	url(r'^logout$', views.logout),

	#仪表盘
	url(r'^dashboard', load.dashboard),

	#发布博文
	url(r'^addNews', load.addNews),
	url(r'^newsList', load.newsList),

	#添加博文
	url(r'^saveNews', saveNews),

	#栏目管理
	url(r'^addClassification', load.addClassification),
	url(r'^classificationList', load.classificationList),

	#栏目列表
	url(r'^getClassificationList', getClassificationList),      #获取栏目

	#添加栏目
	url(r'^getClassification', getClassification),      #获取栏目
	url(r'^saveClassification', saveClassification),    #添加栏目

	#删除栏目
	url(r'^deleteClassification', deleteClassification),  # 添加栏目

	#账户管理
	url(r'^addAccount', load.addAccount),
	url(r'^accountList', load.accountList),

	#添加账号
	url(r'^saveAccount', saveAccount),

	#删除账号
	url(r'^deleteAccount', deleteAccount),

	#账号列表
	url(r'^getAccountList', getAccountList),
	url(r'^getUserName', getUserName),                  #获取用户名称

	#图片管理
	url(r'^addPicture', load.addPicture),
	url(r'^pictureList', load.pictureList),

	#添加图片
	url(r'^savePicture', savePicture),
	url(r'^getPicturePosition', getPicturePosition),   #获取所属栏目

	#删除图片
	url(r'^deletePicture', deletePicture),

	#图片列表
	url(r'^getPictureList', getPictureList),

]