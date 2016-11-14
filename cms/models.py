#coding:utf-8
# model表(总计5个):

from django.db import models

#1 栏目表 classification
class Classification(models.Model):
	classificationId = models.CharField(max_length=36, primary_key=True)
	classificationIdLevel = models.IntegerField()                               #栏目级别
	parentDirectory = models.CharField(max_length=36, blank=True, null=True)    #上级目录
	createTime = models.DateTimeField(auto_now_add=True)                        #创建时间
	classificationName = models.CharField(max_length=50)                        #栏目名称
	classificationFormat = models.IntegerField()                                #栏目内容格式(1:文本,2:图片,3:音乐,4:视频)
	classificationOrder = models.IntegerField()                                 #顺序
	isShow = models.BooleanField(default=1)                                     #是否启用

#2 博文表 news
class News(models.Model):
	newsId = models.CharField(max_length=36, primary_key=True)
	classificationId = models.ForeignKey(Classification)                  #所属栏目
	createTime = models.DateTimeField(auto_now_add=True)                  #创建时间
	title = models.CharField(max_length=50)                               #新闻标题
	briefPic = models.CharField(max_length=80, blank=True, null=True)     #简介图片
	briefNews = models.CharField(max_length=150, blank=True, null=True)   #新闻简介
	content = models.TextField()                                          #内容
	status = models.IntegerField()                                        #状态1:发布,2:暂存
	isTop = models.BooleanField(default=0)                                #是否置顶(0:不置顶)
	alterTime = models.DateTimeField(auto_now_add=True)                   #修改时间
	browseVolume = models.IntegerField(default=0)                         #新闻浏览量

#3 用户表 user
class User(models.Model):
	userId = models.CharField(max_length=36, primary_key=True)
	userAccount = models.CharField(max_length=20)                               #登录账号
	password = models.CharField(max_length=20)                                  #登录密码
	userName = models.CharField(max_length=10)                                  #用户名(前台:昵称)
	state = models.IntegerField()                                               #状态(1:管理员,2:用户)
	createTime = models.DateTimeField(auto_now_add=True)                        #创建时间
	isShow = models.BooleanField(default=1)                                     #是否启用(1:启用)
	sculpture = models.CharField(max_length=50, blank=True, null=True)          #头像url

#4 栏目图片表 picture
class Picture(models.Model):
	pictureId = models.CharField(max_length=36, primary_key=True)
	pictureName = models.CharField(max_length=20)                               #图片名称
	classificationId = models.ForeignKey(Classification)                        #所属栏目
	picturePath = models.CharField(max_length=50)                               #图片路径
	createTime = models.DateTimeField(auto_now_add=True)                        #创建时间
	isShow = models.BooleanField(default=1)                                     #是否启用(1:启用)

#5 评论表 comment
class Comment(models.Model):
	commentId = models.CharField(max_length=36, primary_key=True)
	userId = models.ForeignKey(User)                                            #用户Id
	commentary = models.TextField()                                             #评论内容
	createTime =models.DateTimeField(auto_now_add=True)                         #创建时间
	isShow = models.BooleanField(default=1)                                     #是否启用(1:启用)

