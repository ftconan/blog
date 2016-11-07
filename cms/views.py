# coding:utf-8

from django.shortcuts import render_to_response

def login(req):
	"""
	管理员登录
	:param req:
	:return:
	"""
	return render_to_response("login.html")

# def logout(req):
# 	"""
# 	管理员退出
# 	:param req:
# 	:return:
# 	"""
# 	return response
