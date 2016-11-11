# coding: utf-8

from django.shortcuts import render_to_response
from django.shortcuts import render

def dashboard(req):
	"""
	仪表盘
	:param req:
	:return:
	"""
	return render_to_response("first/dashboard.html")

def addNews(req):
	"""
	添加新闻
	:param req:
	:return:
	"""
	return render_to_response("first/addNews.html")

def newsList(req):
	"""
	添加新闻
	:param req:
	:return:
	"""
	return render_to_response("first/newsList.html")

def addClassification(req):
	"""
	添加栏目
	:param req:
	:return:
	"""
	return render_to_response("first/addClassification.html")

def classificationList(req):
	"""
	栏目列表
	:param req:
	:return:
	"""
	return render_to_response("first/classificationList.html")

def addAccount(req):
	"""
	添加账号
	:param req:
	:return:
	"""
	return render_to_response("first/addAccount.html")

def accountList(req):
	"""
	账号列表
	:param req:
	:return:
	"""
	return render_to_response("first/accountList.html")

def addPicture(req):
	"""
	添加图片
	:param req:
	:return:
	"""
	return render_to_response("first/addPicture.html")

def pictureList(req):
	"""
	图片列表
	:param req:
	:return:
	"""
	return render_to_response("first/pictureList.html")