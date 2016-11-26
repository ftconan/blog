# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import uuid
import json
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from cms.models import Picture, Classification
from django.views.decorators.csrf import csrf_exempt
from PIL import Image

basePath = os.path.dirname(os.path.dirname(__file__))

@csrf_exempt
def getPicturePosition(req):
	"""
	获取所属栏目
	:param req:
	:return:
	"""
	classification = Classification.objects.all().order_by("classificationIdLevel")    #根据栏目级别排序
	List = []
	for obj in classification:
		classificationList = {}
		classificationList["classificationId"] = obj.classificationId
		classificationList["classificationName"] = obj.classificationName
		classificationList["classificationIdLevel"] = obj.classificationIdLevel
		List.append(classificationList)
	return HttpResponse(json.dumps(List))

@csrf_exempt
def savePicture(req):
	"""
	添加图片
	:param req:
	:return:
	"""
	# picture = Picture.objects.filter(pictureId = req.POST["pictureId"])
	picturePosition = req.POST["picturePosition"]          #所属栏目
	pictureName = req.POST["pictureName"]                  #图片名称
	isShow = req.POST["isShow"]                            #是否启用
	if isShow == "true":
		isShow = 1
	else:
		isShow = 0
	#保存图片
	reqfile = req.FILES.get("pictureUrl", False)
	if reqfile != False:
		pictureUrl = "cms/static/img/classPic/"+pictureName
		picturePath = os.path.join(basePath, pictureUrl)
		img = Image.open(reqfile)
		img.thumbnail((700, 700), Image.ANTIALIAS)         #对图片进行等比缩放
		img.save(picturePath, "png")                      #保存图片
	else:
		pictureUrl = ""
	#修改图片
	#添加图片
	pictureId = uuid.uuid1()
	picture = Picture(pictureId=pictureId, pictureName=pictureName, picturePath="/"+pictureUrl, isShow=isShow, classificationId_id=picturePosition)
	picture.save()
	return HttpResponse(1)
