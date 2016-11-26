# coding: utf-8

from django.shortcuts import render_to_response
from views import adminskip, judgeadmin
from cms.models import News, Classification, User, Picture, Comment

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
	firstClassification = Classification.objects.filter(classificationIdLevel=1).order_by("classificationOrder")
	return render_to_response("first/addNews.html", {"firstClassification":firstClassification})

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
	firstClassification = Classification.objects.filter(classificationIdLevel=1).order_by("classificationOrder")
	# if 'update' in req.GET:
	# 	classificationId = req.GET["classificationId"]
	# 	classificationList = {}
	# 	classification = Classification.objects.get(classificationId=classificationId)
	# 	classificationList["classificationId"] = classification.classificationId
	# 	classificationList["classificationName"] = classification.classificationName
	# secondClassification = Classification.objects.filter(classificationIdLevel=2).order_by("classificationOrder")
	return render_to_response("first/addClassification.html", {"firstClassification":firstClassification})

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