# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import uuid
import json
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from cms.models import News
from django.views.decorators.csrf import csrf_exempt
from PIL import Image

basePath = os.path.dirname(os.path.dirname(__file__))

@csrf_exempt
def saveNews(req):
	"""
	保存博文
	:param req:
	:return:
	"""
	secondClassificationId = req.POST["secondClassification"]
	thirdClassificationId = req.POST["thirdClassification"]          #栏目Id
	if thirdClassificationId == "0":
		classificationId = secondClassificationId
	else:
		classificationId = thirdClassificationId
	title = req.POST["title"]                                          #标题
	briefNews = req.POST["briefNews"]                                 #新闻介绍
	content = req.POST["newsContent"]                                 #新闻内容
	pictureName = req.POST["pictureName"]                             #图片名称
	isTop = req.POST["isTop"]                                         #是否置顶
	if isTop == "false":
		isTop = 0
	else:
		isTop = 1
	status = req.POST["status"]                                       #状态
	if status == "saveNews":
		status = 1
	else:
		status = 2
	#保存图片
	reqfile = req.FILES.get("pictureUrl", False)
	if reqfile != False:
		pictureUrl = "cms/static/img/briefPic/"+pictureName
		picturePath = os.path.join(basePath, pictureUrl)
		img = Image.open(reqfile)
		img.thumbnail((700, 700), Image.ANTIALIAS)                    #对图片进行等比缩放
		img.save(picturePath, "png")                                 #保存图片
	else:
		pictureUrl = ""                                              #默认图片
	#添加博文
	newsId = uuid.uuid1()
	if reqfile:
		news = News(newsId=newsId, briefPic="/"+pictureUrl, classificationId_id=classificationId, title=title, briefNews=briefNews, content=content, isTop=isTop, status=status)
		news.save()                                                   #添加博文和图片
		return HttpResponse(1)
	else:
		news = News(newsId=newsId, classificationId_id=classificationId, title=title, briefNews=briefNews, content=content, isTop=isTop, status=status)
		news.save()	                                                  #添加博文不添加图片
		return HttpResponse(2)
