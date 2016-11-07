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