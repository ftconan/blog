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

def album(req):
	"""
	相册
	:param req:
	:return:
	"""
	return render(req, "first/album.html")

def music(req):
	"""
	音乐
	:param req:
	:return:
	"""
	return render(req, "first/music.html")

def film(req):
	"""
	视频
	:param req:
	:return:
	"""
	return render(req, "first/film.html")

def share(req):
	"""
	分享
	:param req:
	:return:
	"""
	return render(req, "first/share.html")

def message(req):
	"""
	留言板
	:param req:
	:return:
	"""
	return render(req, "first/message.html")

def secondBlog(req):
	"""
	博文二级页
	:param req:
	:return:
	"""
	return render(req, "second/secondBlog.html")

def secondAlbum(req):
	"""
	相册二级页
	:param req:
	:return:
	"""
	return render(req, "second/secondAlbum.html")

def secondMusic(req):
	"""
	音乐二级页
	:param req:
	:return:
	"""
	return render(req, "second/secondMusic.html")

def secondFilm(req):
	"""
	视频二级页
	:param req:
	:return:
	"""
	return render(req, "second/secondFilm.html")


