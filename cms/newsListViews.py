# coding=utf-8

import json
from django.http import HttpResponse
from cms.models import News, Classification
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def getNewsList(req):
    """
    获取博文列表
    :param req:
    :return:
    """
    news = News.objects.all()
    List = []
    for obj in news:
        newsList = {}
        newsList["newsId"] = obj.newsId
        newsList["parentDirectory"] = Classification.objects.get(classificationId=obj.classificationId.parentDirectory).classificationName
        newsList["classificationName"] = obj.classificationId.classificationName
        newsList["title"] = obj.title
        newsList["createTime"] = obj.alterTime.strftime('%Y/%m/%d %H:%M:%S')
        if obj.isTop:
            newsList["isTop"] = "是"
        else:
            newsList["isTop"] = "否"
        List.append(newsList)
    return HttpResponse(json.dumps(List))

@csrf_exempt
def deleteNews(req):
    """
    删除博文
    :param req:
    :return:
    """
    newsId = req.POST["newsId"]
    news = News.objects.get(newsId=newsId)
    news.delete()
    return HttpResponse(1)