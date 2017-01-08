# coding=utf-8
from django.shortcuts import render
from cms.models import News, Classification, Picture, Comment

def index(req):
	"""
	首页
	:param req:
	:return:
	"""
	classId1 = Classification.objects.get(classificationName="科技").classificationId                                                  #科技栏目Id
	sicenceBlog = News.objects.filter(classificationId_id=classId1).filter(status=1).order_by("isTop").order_by("-createTime")[:9]    #博文

	classId2 = Classification.objects.get(classificationName="生活").classificationId
	lifeBlog = News.objects.filter(classificationId_id=classId2).filter(status=1).order_by("isTop").order_by("-createTime")[:9]       # 博文

	classId3 = Classification.objects.get(classificationName="体育").classificationId
	sportBlog = News.objects.filter(classificationId_id=classId3).filter(status=1).order_by("isTop").order_by("-createTime")[:9]       # 博文
	return render(req, "first/index.html", {"sicenceBlog": sicenceBlog, "lifeBlog": lifeBlog, "sportBlog": sportBlog})

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
	secondBlog1 = News.objects.filter(title = "美国互联网企业中国之梦褪色：立足也很难赚钱")
	return render(req, "second/secondBlog.html", {"secondBlog1": secondBlog1})

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


