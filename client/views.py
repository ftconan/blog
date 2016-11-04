# coding=utf-8
from django.shortcuts import render

def index(req):
	"""
	首页
	:param req:
	:return:
	"""
	return render(req, "first/index.html")
