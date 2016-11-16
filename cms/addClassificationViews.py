# coding=utf-8

import uuid
import json
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from cms.models import Classification
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def getClassification(req):
	"""
	获取栏目
	:param req:
	:return:
	"""
	parentDirectory = req.POST["parentDirectory"]
	classification = Classification.objects.filter(parentDirectory=parentDirectory)
	List = []
	for obj in classification:
		classificationList = {}
		classificationList["classificationId"] = obj.classificationId
		classificationList["classificationName"] = obj.classificationName
		List.append(classificationList)
	return HttpResponse(json.dumps(List))

@csrf_exempt
def saveClassification(req):
	"""
	添加栏目
	:param req:
	:return:
	"""
	classificationIdLevel = req.POST["classificationIdLevel"]
	classificationFormat = req.POST["classificationFormat"]
	classificationOrder = req.POST["classificationOrder"]
	if req.POST["firstClassText"] != "":                    #添加一级栏目
		classificationName = req.POST["firstClassText"]
		parentDirectory = ""
	elif req.POST["secondClassText"] != "":                 #添加二级栏目
		classificationName = req.POST["secondClassText"]
		parentDirectory = req.POST["firstClassSelect"]
	else:                                                     #添加三级栏目
		classificationName = req.POST["thirdClassText"]
		parentDirectory = req.POST["secondClassSelect"]
	isShow = req.POST["isShow"]
	if isShow == "true":
		isShow = 1
	else:
		isShow = 0
	classificationId = uuid.uuid1()
	classification = Classification(classificationId=classificationId, classificationIdLevel=classificationIdLevel, parentDirectory=parentDirectory, classificationName=classificationName, classificationFormat=classificationFormat, classificationOrder=classificationOrder, isShow=isShow)
	classification.save()
	return HttpResponse(1)