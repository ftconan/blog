# coding=utf-8

import json
from django.http import HttpResponse
from cms.models import Picture, Classification
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def getPictureList(req):
    """
    获取图片列表
    :param req:
    :return:
    """
    picture = Picture.objects.all()
    List = []
    for obj in picture:
        pictureList = {}
        pictureList["pictureId"] = obj.pictureId
        pictureList["classificationId"] = obj.classificationId_id
        pictureList["classificationName"] = obj.classificationId.classificationName
        pictureList["pictureName"] = obj.pictureName
        pictureList["createTime"] = obj.createTime.strftime('%Y/%m/%d %H:%M:%S')
        pictureList["isShow"] = obj.isShow
        if obj.isShow:
            pictureList["isShow"] = "是"
        else:
            pictureList["isShow"] = "否"
        List.append(pictureList)
    return HttpResponse(json.dumps(List))

@csrf_exempt
def deletePicture(req):
    """
    删除图片
    :param req:
    :return:
    """
    pictureId = req.POST["pictureId"]
    account = Picture.objects.get(pictureId = pictureId)
    account.delete()
    return HttpResponse(1)