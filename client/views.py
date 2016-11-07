# coding=utf-8
from django.shortcuts import render

def index(req):
	"""
	首页
	:param req:
	:return:
	"""
	return render(req, "first/index.html")

def blog(req):
	"""
	博文
	:param req:
	:return:
	"""
	return render(req, "first/blog.html")

def secondBlog(req):
	"""
	博文二级页
	:param req:
	:return:
	"""
	return render(req, "second/secondBlog.html")
