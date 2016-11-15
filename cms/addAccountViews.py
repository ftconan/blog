# coding=utf-8

import uuid
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from cms.models import User
from django.views.decorators.csrf import csrf_exempt

#添加账号模块开始
@csrf_exempt
def saveAccount(req):
	"""
	添加账号
	:return:
	"""
	# if req.method =="POST":
	userId = uuid.uuid1()
	userName = req.POST["userName"]
	userAccount = req.POST["userAccount"]
	password = req.POST["password"]
	state = req.POST["state"]
	isShow = req.POST["isShow"]
	if state == "true":
		state = 1
	else:
		state = 0
	if isShow == "true":
		isShow = 1
	else:
		isShow = 0
	#添加账号
	user = User(userId=userId, userName=userName, userAccount=userAccount, password=password, state=state, isShow=isShow)
	user.save()
	return HttpResponse(1)
	# else:
	# 	pass
#添加账号模块结束
